from django.contrib.auth import get_user_model
from rest_framework import serializers

from peshajibi.models import OTPModel
from users.models import CityCorporationUserProfileModel, DivisionUserProfileModel, GuestUserProfileModel

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTPModel
        fields = ['mobile_number']


class AccessOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTPModel
        fields = ['mobile_number']


class GuestProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestUserProfileModel
        exclude = ['user']


class CityProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityCorporationUserProfileModel
        exclude = ['user']


class DivisionProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DivisionUserProfileModel
        exclude = ['user']


class UserSerializer(serializers.ModelSerializer):
    guest_profile = GuestProfileSerializer()
    division_profile = DivisionProfileSerializer()
    city_profile = CityProfileSerializer()

    class Meta:
        model = User
        fields = [
            'id',
            'mobile',
            'photo',
            'guest_profile',
            'city_profile',
            'division_profile',
        ]


class UpdateCityProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityCorporationUserProfileModel
        fields = '__all__'


class UpdateDivisionProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DivisionUserProfileModel
        fields = '__all__'
