from django.contrib.auth import get_user_model
from rest_framework import serializers

from . import models as peshajibi_models

User = get_user_model()

# from apps.users.serializers import UserSerializer


class OTPModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.OTPModel
        fields = ['mobile_number', 'otp_number']


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.DivisionModel
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.DistrictModel
        fields = '__all__'


class UpazilaSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.UpazilaModel
        fields = '__all__'


class UnionSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.UnionModel
        fields = '__all__'


class CityCorporationSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.CityCorporationModel
        fields = '__all__'


class CityCorporationThanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.CityCorporationThanaModel
        fields = '__all__'


class ProfessionCategorySerializer(serializers.ModelSerializer):
    profession_count = serializers.IntegerField()

    class Meta:
        model = peshajibi_models.ProfessionCatModel
        fields = ['id', 'name_eng', 'name_bng', 'profession_count', 'created_at', 'updated_at']


class ProfessionSerializer(serializers.ModelSerializer):
    user_count = serializers.IntegerField()

    class Meta:
        model = peshajibi_models.ProfessionModel
        fields = ['id', 'name_eng', 'name_bng', 'profession_cat', 'user_count', 'created_at', 'updated_at']


class BasicProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.ProfessionModel
        fields = ['id', 'name_bng', 'name_eng']


class BasicProfessionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.ProfessionCatModel
        fields = ['id', 'name_bng', 'name_eng']


# class JobTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = peshajibi_models.JobTypeModel
#         fields = '__all__'


# class GenericAdsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = peshajibi_models.GenericAdsServiceModel
#         fields = '__all__'


# class TransportAdsSerializer(serializers.ModelSerializer):
#     from_division = DivisionSerializer()
#     to_division = DivisionSerializer()
#     from_district = DistrictSerializer()
#     to_district = DistrictSerializer()
#     from_upazila = UpazilaSerializer()
#     to_upazila = UpazilaSerializer()

#     class Meta:
#         model = peshajibi_models.TransportAdsService
#         fields = '__all__'


# class ContentObjectRelatedField(serializers.RelatedField):
#     """
#     A custom field to use for the `content_object` generic relationship.
#     """

#     def to_representation(self, value):
#         """
#         Serialize tagged objects to a simple textual representation.
#         """
#         if isinstance(value, peshajibi_models.GenericAdsServiceModel):
#             return GenericAdsSerializer(value).data
#         elif isinstance(value, peshajibi_models.TransportAdsService):
#             return TransportAdsSerializer(value).data

#         else:
#             return 'unknown'


# class AdsSerializer(serializers.ModelSerializer):
#     content_object = ContentObjectRelatedField(read_only=True)

#     class Meta:
#         model = peshajibi_models.AdsServicesModel
#         fields = "__all__"


# class TransportAdsCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = peshajibi_models.TransportAdsService
#         fields = '__all__'


# class AdsServiceTypeSerializer(serializers.Serializer):
#     service_type = serializers.CharField(max_length=50)


# Start update profile API serializers


class UpdateProfileProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.ProfessionModel
        fields = ['id', 'name_bng', 'name_eng']


class UpdateProfileDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.DivisionModel
        fields = ['id', 'name_bng', 'name_eng']


class UpdateProfileDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.DistrictModel
        fields = ['id', 'name_bng', 'name_eng']


class UpdateProfileUpazilaSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.UpazilaModel
        fields = ['id', 'name_bng', 'name_eng']


class UpdateProfileUnionSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.UnionModel
        fields = ['id', 'name_bng', 'name_eng']


class UpdateProfileCityCorporationSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.CityCorporationModel
        fields = ['id', 'name_bng', 'name_eng']


class UpdateProfileCityCorporationThanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.CityCorporationThanaModel
        fields = ['id', 'name_bng', 'name_eng']


# End update profile serializers


class AdsServicesScehmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.AdsServiceTypeSchemaModel
        fields = "__all__"


class BasicDivisionSerializr(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.DivisionModel
        fields = ['id', 'name_bng', 'name_eng']


class BasicDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.DistrictModel
        fields = ['id', 'name_bng', 'name_eng']


class BasicUpazilaSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.UpazilaModel
        fields = ['id', 'name_bng', 'name_eng']


class BasicUnionSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.UnionModel
        fields = ['id', 'name_bng', 'name_eng']


class AdsListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'mobile']


class AdsListSerializer(serializers.ModelSerializer):
    from_division = BasicDivisionSerializr()
    to_division = BasicDivisionSerializr()
    from_district = BasicDistrictSerializer()
    to_district = BasicDistrictSerializer()
    from_upazila = BasicUpazilaSerializer()
    to_upazila = BasicUpazilaSerializer()
    profession = BasicProfessionSerializer()
    ads_type = BasicProfessionCategorySerializer()
    user = AdsListUserSerializer()

    class Meta:
        model = peshajibi_models.Ads
        fields = "__all__"


class AdsCreateTransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.Ads
        fields = [
            'user',
            'profession',
            'ads_type',
            'service_type',
            'service_medium_or_item',
            'from_division',
            'to_division',
            'from_district',
            'to_district',
            'from_upazila',
            'to_upazila',
            'product_name',
            'product_weight',
            'notice_period_days',
            'cost',
            'is_negotiable',
            'description',
        ]


class AdsCreateGenericSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.Ads
        fields = [
            'user',
            'profession',
            'ads_type',
            'service_type',
            'service_medium_or_item',
            'notice_period_days',
            'cost',
            'description',
        ]
