import math
import random

from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from peshajibi.models import OTPModel

from .serializers import (
    RegistrationSerializer,
    UpdateCityProfileSerializer,
    UpdateDivisionProfileSerializer,
    UserSerializer,
)

User = get_user_model()


def generate_otp():
    digits = [i for i in range(0, 10)]
    random_str = ""
    for i in range(6):
        index = math.floor(random.random() * 10)
        random_str += str(digits[index])

    return random_str


class UserListAPI(generics.ListCreateAPIView):
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
            response = {'status': 'failed', 'error': 'wrong profile type'}
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
