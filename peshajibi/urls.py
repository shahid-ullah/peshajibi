from django.urls import path

from . import apis

urlpatterns = [
    path('verify_otp/', apis.VerifyOTPAPI.as_view(), name='verify_otp'),
    path('otp/', apis.AccessOTPAPI.as_view(), name='otp'),
    path('division_list/', apis.DivisionListAPI.as_view(), name='division_list'),
    path('district_list/', apis.DistrictListAPI.as_view(), name='district_list'),
    path('upazila_list/', apis.UpazilaListAPI.as_view(), name='upazila_list'),
    path('union_list/', apis.UnionListAPI.as_view(), name='union_list'),
    path('city_corporation_list/', apis.CityCorporationListAPI.as_view(), name='city_corporation_list'),
    path(
        'city_corporation_thana_list/', apis.CityCorporationThanaListAPI.as_view(), name='city_corporation_thana_list'
    ),
    path('profession_cat_list/', apis.ProfessionCategoryListAPI.as_view(), name='profession_cat_list'),
    path('profession_list/', apis.ProfessionListAPI.as_view(), name='profession_list'),
    path('job_type_list/', apis.JobTypeListAPI.as_view(), name='job_type_list'),
]
