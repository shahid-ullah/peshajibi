from django.contrib import admin

from .models import (
    AdsServicesModel,
    AdsServiceTypeSchemaModel,
    CityCorporationModel,
    CityCorporationThanaModel,
    DistrictModel,
    DivisionModel,
    GenericAdsServiceModel,
    JobTypeModel,
    OTPModel,
    ProfessionCatModel,
    ProfessionModel,
    TransportAdsService,
    UnionModel,
    UpazilaModel,
)

admin.site.register(OTPModel)
admin.site.register(DivisionModel)
admin.site.register(DistrictModel)
admin.site.register(UpazilaModel)
admin.site.register(UnionModel)
admin.site.register(ProfessionCatModel)
admin.site.register(ProfessionModel)
admin.site.register(CityCorporationModel)
admin.site.register(CityCorporationThanaModel)
admin.site.register(JobTypeModel)
admin.site.register(AdsServicesModel)
admin.site.register(GenericAdsServiceModel)
admin.site.register(TransportAdsService)
admin.site.register(AdsServiceTypeSchemaModel)
