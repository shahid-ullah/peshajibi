import math
import random
import re

from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from peshajibi.models import OTPModel
from peshajibi.utils import StandardResultsSetPagination

from .serializers import (
    FavouriteUserIDsSerializer,
    RegistrationSerializer,
    UpdateCityProfileSerializer,
    UpdateDivisionProfileSerializer,
    UserSerializer,
)

ids_regex = re.compile(r'\d+')
User = get_user_model()


def generate_otp():
    digits = [i for i in range(0, 10)]
    random_str = ""
    for i in range(6):
        index = math.floor(random.random() * 10)
        random_str += str(digits[index])

    return random_str


class UserListAPI(generics.ListCreateAPIView):
    pagination_class = StandardResultsSetPagination
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.prefetch_related('guest_profile', 'city_profile', 'division_profile')
    serializer_class = UserSerializer


class UserDetailAPI(generics.RetrieveAPIView):
    response_class = []
    queryset = User.objects.prefetch_related('guest_profile', 'city_profile', 'division_profile')
    serializer_class = UserSerializer


class RegistrationAPI(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        serializer = RegistrationSerializer(data=request.POST)

        if serializer.is_valid():
            mobile_number = serializer.validated_data['mobile_number']
            try:
                OTPModel.objects.get(mobile_number=mobile_number)
                otp_number = generate_otp()
            except OTPModel.DoesNotExist:
                otp_number = generate_otp()
                OTPModel.objects.create(mobile_number=mobile_number, otp_number=otp_number)

            response = {'status': 'success'}
            return Response(response)
        else:
            response = {'status': 'failed', 'error': serializer.errors}
            return Response(response)


class ProfileUpdateAPI(APIView):
    permission_classes = [IsAuthenticated]
    profile_type_serializer = {
        'division_profile': UpdateDivisionProfileSerializer,
        'city_profile': UpdateCityProfileSerializer,
    }

    def post(self, request, format=None):
        """
        update user profile.
        """

        user_id = request.POST.get('user')

        # check profile type
        try:
            profile_type = request.POST['profile_type']
        except KeyError:
            response = {'status': 'failed', 'error': 'profile_type missing'}
            return Response(response)
        # check user account
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            response = {'status': 'failed', 'error': 'user account not found'}
            return Response(response)

        # get profile type serializer
        serializer_class = self.profile_type_serializer.get(profile_type)
        if not serializer_class:
            response = {'status': 'failed', 'error': 'wrong profile type. choices: division_profile, city_profile'}
            return Response(response)

        # get profile instance
        try:
            profile_instance = getattr(user, profile_type)
        except:
            profile_instance = None

        if profile_instance is not None:
            serializer = serializer_class(profile_instance, data=request.POST)
        else:
            serializer = serializer_class(None, data=request.POST)

        if serializer.is_valid():
            serializer.save()
            response = {'status': 'success', 'data': serializer.data}
            return Response(response)
        else:
            response = {'status': 'failed', 'error': serializer.errors}
            return Response(response)


class FavouriteUserListAPI(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        self.queryset = self.request.user.favourites.all()
        return self.list(request, *args, **kwargs)


class FavouriteUserAddRemove(APIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = FavouriteUserIDsSerializer

    def post(self, request, format=None):
        serializer = FavouriteUserIDsSerializer(data=request.data)
        if serializer.is_valid():
            ids_string = serializer.validated_data['ids']
            ids = ids_regex.findall(ids_string)
            favourite_users = list(self.queryset.filter(id__in=ids))
            for user in favourite_users:
                self.request.user.favourites.add(user)
            return Response({'status': 'success', 'add_ids': ids})

        response = {'status': 'failed', 'errors': serializer.errors}

        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        serializer = FavouriteUserIDsSerializer(data=request.data)
        if serializer.is_valid():
            ids_string = serializer.validated_data['ids']
            ids = ids_regex.findall(ids_string)
            favourite_users = list(self.queryset.filter(id__in=ids))
            for user in favourite_users:
                self.request.user.favourites.remove(user)
            return Response({'status': 'success', 'removed_ids': ids})

        response = {'status': 'failed', 'errors': serializer.errors}

        return Response(response, status=status.HTTP_400_BAD_REQUEST)
