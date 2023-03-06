import copy
import math
import random
import re

from django.contrib.auth import get_user_model
from django.db.models.query import QuerySet
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.utils import StandardResultsSetPagination
from apps.peshajibi.models import OTPModel

from .serializers import (
    AccountUpdateSerializer,
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


class UserListAPI(generics.ListAPIView):
    pagination_class = StandardResultsSetPagination
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.prefetch_related('guest_profile', 'city_profile', 'division_profile')
    serializer_class = UserSerializer

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method." % self.__class__.__name__
        )

        queryset = self.queryset
        profession_id = self.request.GET.get('profession')
        try:
            if profession_id:
                queryset = queryset.filter(division_profile__profession__id=profession_id)
        except:
            pass
        queryset = queryset.filter()
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset


class UserDetailAPI(generics.RetrieveAPIView):
    response_class = []
    queryset = User.objects.prefetch_related('guest_profile', 'city_profile', 'division_profile')
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response_data = copy.deepcopy(serializer.data)
        response_data['status'] = 'success'
        return Response(response_data)


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

    def post(self, request, format=None):
        """
        update user profile.
        """
        data = copy.deepcopy(request.POST)
        data['user'] = request.user.id

        division_profile = getattr(request.user, 'division_profile', None)
        if division_profile is not None:
            division_profile_serializer = UpdateDivisionProfileSerializer(division_profile, data=data)
        else:
            division_profile_serializer = UpdateDivisionProfileSerializer(data=data)
        if division_profile_serializer.is_valid():
            division_profile_serializer.save()
            division_errors = {}
        else:
            division_errors = division_profile_serializer.errors

        city_profile = getattr(request.user, 'city_profile', None)

        if city_profile is not None:
            city_profile_serializer = UpdateCityProfileSerializer(city_profile, data=data)
        else:
            city_profile_serializer = UpdateCityProfileSerializer(data=data)

        if city_profile_serializer.is_valid():
            city_profile_serializer.save()
            city_errors = {}
        else:
            city_errors = city_profile_serializer.errors

        account_serializer = AccountUpdateSerializer(request.user, data=data)
        if account_serializer.is_valid():
            account_serializer.save()
            account_errors = {}
        else:
            account_errors = account_serializer.errors

        user_serializer = UserSerializer(request.user)
        user_info = user_serializer.data
        try:
            photo_url = request.build_absolute_uri(request.user.photo.url)
            user_info['photo'] = photo_url
        except:
            pass
        response = {
            'status': 'success',
            'user_info': user_info,
            'errors': [
                {'account_errors': account_errors},
                {'division_errors': division_errors},
                {'city_errors': city_errors},
            ],
        }
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
