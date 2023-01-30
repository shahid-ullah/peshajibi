from django.contrib import admin

from .models import (
    CityCorporationModel,
    CityCorporationThanaModel,
    DistrictModel,
    DivisionModel,
    JobTypeModel,
    OTPModel,
    ProfessionCatModel,
    ProfessionModel,
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
