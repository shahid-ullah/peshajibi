from rest_framework import serializers

from . import models as peshajibi_models


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
    class Meta:
        model = peshajibi_models.ProfessionCatModel
        fields = '__all__'


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.ProfessionModel
        fields = '__all__'


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = peshajibi_models.JobTypeModel
        fields = '__all__'
