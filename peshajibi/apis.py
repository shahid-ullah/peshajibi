from django.contrib.auth import get_user_model
from rest_framework import generics, mixins
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from peshajibi.models import (
    CityCorporationModel,
    CityCorporationThanaModel,
    DistrictModel,
    JobTypeModel,
    OTPModel,
    ProfessionCatModel,
    ProfessionModel,
    UnionModel,
    UpazilaModel,
)
from users.models import AccountsModel, DivisionModel, UserTypeModel
from users.serializers import AccessOTPSerializer

from . import serializers as peshajibi_serializers
from .utils import StandardResultsSetPagination

User = get_user_model()


class VerifyOTPAPI(APIView):
    def post(self, request, format=None):
        """
        Verify OTP and save the user if not exist.
        """
        serializer = peshajibi_serializers.OTPModelSerializer(data=request.POST)

        if serializer.is_valid():
            mobile_number = serializer.validated_data.get('mobile_number')
            otp_number = serializer.validated_data.get('otp_number')
        else:
            response = {'status': 'Invalid', 'error': serializer.errors}
            return Response(response)

        otp_objects = OTPModel.objects.filter(mobile_number=mobile_number, otp_number=otp_number)

        if otp_objects.exists():
            user_type = UserTypeModel.objects.get_or_create(id=2)[0]
            user = AccountsModel.objects.get_or_create(mobile=mobile_number)[0]
            # breakpoint()
            user.user_type.add(user_type)
            token = Token.objects.get_or_create(user=user)[0].key
            response = {
                'status': 'Valid',
                'user_info': {
                    'id': user.id,
                    'mobile': user.mobile,
                },
                'token': token,
            }
        else:
            response = {'status': 'Invalid', 'error': 'No OTP found'}

        return Response(response)


class AccessOTPAPI(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request, format=None):
        """
        Return user OTP.
        """
        serializer = AccessOTPSerializer(data=request.POST)

        if serializer.is_valid():
            mobile_number = serializer.validated_data['mobile_number']
            otp_objects = OTPModel.objects.filter(mobile_number=mobile_number)
            if otp_objects.exists():
                otp_number = otp_objects[0].otp_number
                response = {'status': 'success', 'otp_number': otp_number}
            else:
                response = {'status': 'failed', 'error': 'No OTP found'}
        else:
            response = {'status': 'failed', 'error': serializer.errors}

        return Response(response)


class DivisionListAPI(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = DivisionModel.objects.all()
    serializer_class = peshajibi_serializers.DivisionSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DistrictListAPI(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = DistrictModel.objects.all()
    serializer_class = peshajibi_serializers.DistrictSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        division_id = request.GET.get('division')
        if division_id:
            self.queryset = self.queryset.filter(division=division_id)

        return self.list(request, *args, **kwargs)


class UpazilaListAPI(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = UpazilaModel.objects.all()
    serializer_class = peshajibi_serializers.UpazilaSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        district_id = request.GET.get('district')
        if district_id:
            self.queryset = self.queryset.filter(district=district_id)
        return self.list(request, *args, **kwargs)


class UnionListAPI(mixins.ListModelMixin, generics.GenericAPIView):
    # permission_classes = [IsAdminUser]
    queryset = UnionModel.objects.all()
    serializer_class = peshajibi_serializers.UnionSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        upazila_id = request.GET.get('upazila')
        if upazila_id:
            self.queryset = self.queryset.filter(upazila=upazila_id)
        return self.list(request, *args, **kwargs)


class CityCorporationListAPI(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = CityCorporationModel.objects.all()
    serializer_class = peshajibi_serializers.CityCorporationSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CityCorporationThanaListAPI(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = CityCorporationThanaModel.objects.all()
    serializer_class = peshajibi_serializers.CityCorporationThanaSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        city_corporation_id = request.GET.get('city_corporation')
        if city_corporation_id:
            self.queryset = self.queryset.filter(city_corporation=city_corporation_id)
        return self.list(request, *args, **kwargs)


class ProfessionCategoryListAPI(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = ProfessionCatModel.objects.all()
    serializer_class = peshajibi_serializers.ProfessionCategorySerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProfessionListAPI(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = ProfessionModel.objects.all()
    serializer_class = peshajibi_serializers.ProfessionSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        profession_cat_id = request.GET.get('profession_cat')
        if profession_cat_id:
            self.queryset = self.queryset.filter(profession_cat=profession_cat_id)
        return self.list(request, *args, **kwargs)


class JobTypeListAPI(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = JobTypeModel.objects.all()
    serializer_class = peshajibi_serializers.JobTypeSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
