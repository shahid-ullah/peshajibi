from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.peshajibi.models import OTPModel
from apps.users.models import (
    AccountsModel,
    CityCorporationUserProfileModel,
    DivisionUserProfileModel,
    GuestUserProfileModel,
)

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
            'username',
            'username_eng',
            'username_bng',
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


class FavouriteUserIDsSerializer(serializers.Serializer):
    ids = serializers.CharField(max_length=100)


class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsModel
        fields = [
            'username',
            'email',
            'username_eng',
            'username_bng',
        ]
