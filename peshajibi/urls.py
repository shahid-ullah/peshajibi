from django.urls import path

from . import apis

urlpatterns = [
    path('verify_otp/', apis.VerifyOTPAPI.as_view(), name='verify_otp'),
    path('otp/', apis.AccessOTPAPI.as_view(), name='otp'),
    path('divisions/', apis.DivisionListAPI.as_view(), name='division_list'),
    path('districts/', apis.DistrictListAPI.as_view(), name='district_list'),
    path('upazilas/', apis.UpazilaListAPI.as_view(), name='upazila_list'),
    path('unions/', apis.UnionListAPI.as_view(), name='union_list'),
    path('city_corporations/', apis.CityCorporationListAPI.as_view(), name='city_corporation_list'),
    path('city_corporation_thanas/', apis.CityCorporationThanaListAPI.as_view(), name='city_corporation_thana_list'),
    path('profession_cats/', apis.ProfessionCategoryListAPI.as_view(), name='profession_cat_list'),
    path('professions/', apis.ProfessionListAPI.as_view(), name='profession_list'),
    path('job_types/', apis.JobTypeListAPI.as_view(), name='job_type_list'),
]
