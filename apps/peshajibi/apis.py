from copy import deepcopy
from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from rest_framework import generics, mixins
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.utils import StandardResultsSetPagination
from apps.peshajibi.models import (  # AdsServicesModel,; JobTypeModel,
    Ads,
    AdsServiceTypeSchemaModel,
    CityCorporationModel,
    CityCorporationThanaModel,
    DistrictModel,
    OTPModel,
    ProfessionCatModel,
    ProfessionModel,
    UnionModel,
    UpazilaModel,
)
from apps.users.models import AccountsModel, BearerAuthentication, DivisionModel, UserTypeModel
from apps.users.serializers import AccessOTPSerializer, UserSerializer

from . import serializers as peshajibi_serializers

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
            user.user_type.add(user_type)
            token = Token.objects.get_or_create(user=user)[0].key
            user_serializer = UserSerializer(user)
            user_info = user_serializer.data
            try:
                photo_url = request.build_absolute_uri(request.user.photo.url)
                user_info['photo'] = photo_url
            except:
                pass

            response = {
                'status': 'Valid',
                'user_info': user_info,
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
    queryset = ProfessionCatModel.objects.all().order_by('id')
    serializer_class = peshajibi_serializers.ProfessionCategorySerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        self.queryset = self.queryset.annotate(profession_count=Count('professionmodel'))
        return self.list(request, *args, **kwargs)


class ProfessionListAPI(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = ProfessionModel.objects.all().order_by('id')
    serializer_class = peshajibi_serializers.ProfessionSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        profession_cat_id = request.GET.get('profession_cat')
        if profession_cat_id:
            self.queryset = self.queryset.filter(profession_cat=profession_cat_id)
        self.queryset = self.queryset.annotate(user_count=Count('citycorporationuserprofilemodel'))
        return self.list(request, *args, **kwargs)


# class JobTypeListAPI(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = JobTypeModel.objects.all()
#     serializer_class = peshajibi_serializers.JobTypeSerializer
#     pagination_class = StandardResultsSetPagination

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


# class AdsListAPI(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = AdsServicesModel.objects.all()
#     serializer_class = peshajibi_serializers.AdsSerializer
#     pagination_class = StandardResultsSetPagination

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


# class AdsCreateAPI(generics.CreateAPIView):
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAdminUser]

#     ads_service_type_serializer = {
#         'transport': peshajibi_serializers.TransportAdsCreateSerializer,
#         'generic': peshajibi_serializers.GenericAdsSerializer,
#     }

#     def post(self, request, format=None):
#         """ """
#         service_type_serializer = peshajibi_serializers.AdsServiceTypeSerializer(data=request.POST)
#         if not service_type_serializer.is_valid():
#             response = {'status': 'failed', 'error': service_type_serializer.errors}
#             return Response(response)

#         service_type = service_type_serializer.validated_data['service_type']
#         serializer_class = self.ads_service_type_serializer.get(service_type)
#         if not serializer_class:
#             response = {'status': 'failed', 'error': 'wrong transport type. options: transport, generic'}
#             return Response(response)

#         serializer = serializer_class(data=request.POST)

#         if serializer.is_valid():
#             # serializer.save()
#             # add logic for adding this object to base ads service object
#             response = {'status': 'success'}
#         else:
#             response = {'status': 'failed', 'error': serializer.errors}

#         return Response(response)


# class AdsRetrieveDestroyAPI(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = AdsServicesModel.objects.all()
#     serializer_class = peshajibi_serializers.AdsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         response = {'status': 'success'}
#         return Response(response, status=status.HTTP_204_NO_CONTENT)

#     def perform_destroy(self, instance):
#         try:
#             instance.content_object.delete()
#         except:
#             pass
#         instance.delete()


class AdsServiceSchemaListAPI(generics.ListAPIView):
    pagination_class = StandardResultsSetPagination
    # permission_classes = [IsAuthenticated]
    queryset = AdsServiceTypeSchemaModel.objects.all()
    serializer_class = peshajibi_serializers.AdsServicesScehmaSerializer

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method." % self.__class__.__name__
        )

        queryset = self.queryset
        service_level = self.request.GET.get('service_level')
        try:
            if service_level:
                queryset = queryset.filter(service_level=service_level)
        except:
            pass
        queryset = queryset.filter()
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset


class AdsListAPI(generics.ListAPIView):
    pagination_class = StandardResultsSetPagination
    # permission_classes = [IsAuthenticated]
    queryset = Ads.objects.all()
    serializer_class = peshajibi_serializers.AdsListSerializer


class AdsCreateAPI(generics.CreateAPIView):
    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        """ """
        data = deepcopy(request.data)
        data['user'] = request.user.id
        try:
            data['profession'] = request.user.city_profile.profession.id
        except:
            return Response({'status': 'Failed', 'errors': ['user"s must have profession id']})

        # ads_type_level = request.POST.get('ads_type_level', None)
        # if not ads_type_level:
        #     return Response({'status': 'Failed', 'errors': ['ads type level missing. e.g: ads_type_level: transport']})

        transport_serializer_class = peshajibi_serializers.AdsCreateTransportSerializer
        # generic_serializer_class = peshajibi_serializers.AdsCreateGenericSerializer
        transport_serializer = transport_serializer_class(data=data)
        # generic_serializer = generic_serializer_class(data=data)

        # error_count = 0
        if transport_serializer.is_valid():
            model_obj = transport_serializer.save()
            try:
                notice_period_days = int(model_obj.notice_period_days)
                model_obj.expire_date = date.today() + timedelta(days=notice_period_days)
                model_obj.save()
            except:
                pass
        else:
            return Response({'status': 'Failed', 'errors': transport_serializer.errors})
            # error_count = error_count + 1
            # if generic_serializer.is_valid():
            #     model_obj = generic_serializer.save()
            #     try:
            #         notice_period_days = int(model_obj.notice_period_days)
            #         model_obj.expire_date = date.today() + timedelta(days=notice_period_days)
            #         model_obj.save()
            #     except:
            #         pass
            # else:
            #     error_count = error_count + 1

        # if error_count == 2:
        # return Response({'status': 'Failed', 'errors': [transport_serializer.errors, generic_serializer.errors]})

        sr = peshajibi_serializers.AdsListSerializer(model_obj)
        return Response({'status': 'success', 'result': sr.data})
