from django.contrib.auth import get_user_model
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from apps.peshajibi.models import OTPModel
from apps.peshajibi.serializers import (
    CityCorporationSerializer,
    CityCorporationThanaSerializer,
    DistrictSerializer,
    DivisionSerializer,
    ProfessionSerializer,
    UnionSerializer,
    UpazilaSerializer,
)
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
    profession = ProfessionSerializer()
    present_city = CityCorporationSerializer()
    permanent_city = CityCorporationSerializer()
    present_thana = CityCorporationThanaSerializer()
    permanent_thana = CityCorporationThanaSerializer()

    class Meta:
        model = CityCorporationUserProfileModel
        exclude = ['user', 'created_at', 'updated_at']


class DivisionProfileSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer()
    present_division = DivisionSerializer()
    permanent_division = DivisionSerializer()
    present_district = DistrictSerializer()
    permanent_district = DistrictSerializer()
    present_upazila = UpazilaSerializer()
    permanent_upazila = UpazilaSerializer()
    present_union = UnionSerializer()
    permanent_union = UnionSerializer()

    class Meta:
        model = DivisionUserProfileModel
        exclude = ['user', 'created_at', 'updated_at']


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
            'is_donate_blood',
            'is_share_profile',
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
    photo = Base64ImageField(required=False)

    class Meta:
        model = AccountsModel
        fields = [
            'username',
            'email',
            'photo',
            'username_eng',
            'username_bng',
            'is_donate_blood',
            'is_share_profile',
        ]
