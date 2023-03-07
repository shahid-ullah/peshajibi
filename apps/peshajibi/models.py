from django.conf import settings

# from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
# from django.contrib.contenttypes.models import ContentType
from django.db import models


def EMPTY_DICTIONARY():
    return {}


class OTPModel(models.Model):
    mobile_number = models.CharField(max_length=20, db_index=True)
    user_type = models.CharField(max_length=50, blank=True, null=True)
    otp_number = models.IntegerField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "otp_storage"
        ordering = ['id']

    def __str__(self):
        return f'{self.mobile_number} {self.user_type}'


class DivisionModel(models.Model):
    name_bng = models.CharField(max_length=100, blank=True, null=True)
    name_eng = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "division"
        ordering = ['id']

    def __str__(self):
        return f'{self.name_bng} {self.name_eng}'


class DistrictModel(models.Model):
    name_bng = models.CharField(max_length=100, blank=True, null=True)
    name_eng = models.CharField(max_length=100, blank=True, null=True)
    division = models.ForeignKey(DivisionModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "district"
        ordering = ['id']

    def __str__(self):
        return f'{self.name_bng} {self.name_eng}'


class UpazilaModel(models.Model):
    name_bng = models.CharField(max_length=100, blank=True, null=True)
    name_eng = models.CharField(max_length=100, blank=True, null=True)
    district = models.ForeignKey(DistrictModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "upazila"
        ordering = ['id']

    def __str__(self):
        return f'{self.name_bng} {self.name_eng}'


class UnionModel(models.Model):
    name_bng = models.CharField(max_length=100, blank=True, null=True)
    name_eng = models.CharField(max_length=100, blank=True, null=True)
    upazila = models.ForeignKey(UpazilaModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "union"
        ordering = ['id']

    def __str__(self):
        return f'{self.name_bng} {self.name_eng}'


class CityCorporationModel(models.Model):
    name_bng = models.CharField(max_length=100, blank=True, null=True)
    name_eng = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "city_corporation"
        ordering = ['id']

    def __str__(self):
        return f'{self.name_bng} {self.name_eng}'


class CityCorporationThanaModel(models.Model):
    name_bng = models.CharField(max_length=100, blank=True, null=True)
    name_eng = models.CharField(max_length=100, blank=True, null=True)
    city_corporation = models.ForeignKey(CityCorporationModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "city_corporation_thana"
        ordering = ['id']

    def __str__(self):
        return f'{self.name_bng} {self.name_eng}'


class ProfessionCatModel(models.Model):
    name_bng = models.CharField(max_length=100, blank=True, null=True)
    name_eng = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "profession_category"
        # ordering = ['id']

    def __str__(self):
        return f'{self.name_bng} {self.name_eng}'


class ProfessionModel(models.Model):
    name_bng = models.CharField(max_length=100, blank=True, null=True)
    name_eng = models.CharField(max_length=100, blank=True, null=True)
    profession_cat = models.ForeignKey(ProfessionCatModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "profession"
        # ordering = ['id']

    def __str__(self):
        return f'{self.name_bng} {self.name_eng}'


# class JobTypeModel(models.Model):
#     name_bng = models.CharField(max_length=100, blank=True, null=True)
#     name_eng = models.CharField(max_length=100, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True, editable=False)
#     updated_at = models.DateTimeField(auto_now=True, editable=False)

#     class Meta:
#         db_table = "job_type"
#         ordering = ['id']

#     def __str__(self):
#         return f'{self.name_bng} {self.name_eng}'


# class AdsServicesModel(models.Model):
#     ads_type = models.CharField(max_length=50)
#     profession_cat = models.ForeignKey(ProfessionCatModel, related_name="ads_services", on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='my_ads', on_delete=models.CASCADE)
#     is_negotiable = models.BooleanField(default=False)
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey()
#     created_at = models.DateTimeField(auto_now_add=True, editable=False)
#     updated_at = models.DateTimeField(auto_now=True, editable=False)

#     class Meta:
#         db_table = 'ads_services'
#         ordering = ['-id']

#     def __str__(self):
#         return f'{self.ads_type}'


# class TransportAdsService(models.Model):
#     from_division = models.ForeignKey(DivisionModel, related_name='from_division_transports', on_delete=models.CASCADE)
#     to_division = models.ForeignKey(DivisionModel, related_name='to_division_transports', on_delete=models.CASCADE)
#     from_district = models.ForeignKey(DistrictModel, related_name='from_district_transports', on_delete=models.CASCADE)
#     to_district = models.ForeignKey(DistrictModel, related_name='to_district_transports', on_delete=models.CASCADE)
#     from_upazila = models.ForeignKey(UpazilaModel, related_name='from_upazila_transports', on_delete=models.CASCADE)
#     to_upazila = models.ForeignKey(UpazilaModel, related_name='to_upazila_transports', on_delete=models.CASCADE)
#     ads_services = GenericRelation(AdsServicesModel, related_query_name='transport_ads')
#     transport_medium = models.CharField(max_length=100, db_index=True)
#     product_name = models.CharField(max_length=100, db_index=True)
#     product_weight = models.CharField(max_length=100, blank=True)
#     cost = models.DecimalField(default=0, decimal_places=2, max_digits=50)
#     created_at = models.DateTimeField(auto_now_add=True, editable=False)
#     updated_at = models.DateTimeField(auto_now=True, editable=False)

#     class Meta:
#         db_table = 'transport_ads_services'
#         ordering = ['-id']


# class GenericAdsServiceModel(models.Model):
#     work_type = models.CharField(max_length=50)
#     cost = models.DecimalField(default=0, decimal_places=2, max_digits=50)
#     description = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, editable=False)
#     updated_at = models.DateTimeField(auto_now=True, editable=False)
#     ads_services = GenericRelation(AdsServicesModel, related_query_name='generic_ads')

#     class Meta:
#         db_table = 'generic_ads_services'
#         ordering = ['-id']


class AdsServiceTypeSchemaModel(models.Model):
    service_id = models.PositiveIntegerField(db_index=True)
    service_level = models.CharField(max_length=100)
    key = models.CharField(max_length=50)
    level = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    value = models.JSONField(default=EMPTY_DICTIONARY, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'service_id: {self.service_id}  key: {self.key}'

    class Meta:
        db_table = 'ads_service_type_schema'
        ordering = ['service_id']


class Ads(models.Model):

    SERVICE_CHOICES = (
        ('offer_service', 'সেবা দিতে চাই'),
        ('take_service', 'সেবা নিতে চাই'),
    )
    SERVICE_MEDIUM_OR_ITEM_CHOICES = (
        ('fridge', 'ফ্রিজ'),
        ('mobile', 'মোবাইল'),
        ('microbus', 'মাইক্রোবাস'),
        ('motorcycle', 'মোটর সাইকেল'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_ads')
    profession = models.ForeignKey(ProfessionModel, on_delete=models.CASCADE, related_name='ads')
    ads_type = models.ForeignKey(ProfessionCatModel, on_delete=models.CASCADE, related_name='ads')
    service_type = models.CharField(choices=SERVICE_CHOICES, max_length=100)
    from_division = models.ForeignKey(
        DivisionModel, related_name='from_division_transports', on_delete=models.CASCADE, blank=True, null=True
    )
    to_division = models.ForeignKey(
        DivisionModel, related_name='to_division_transports', on_delete=models.CASCADE, blank=True, null=True
    )
    from_district = models.ForeignKey(
        DistrictModel, related_name='from_district_transports', on_delete=models.CASCADE, blank=True, null=True
    )
    to_district = models.ForeignKey(
        DistrictModel, related_name='to_district_transports', on_delete=models.CASCADE, blank=True, null=True
    )
    from_upazila = models.ForeignKey(
        UpazilaModel, related_name='from_upazila_transports', on_delete=models.CASCADE, blank=True, null=True
    )
    to_upazila = models.ForeignKey(
        UpazilaModel, related_name='to_upazila_transports', on_delete=models.CASCADE, blank=True, null=True
    )
    service_medium_or_item = models.CharField(
        choices=SERVICE_MEDIUM_OR_ITEM_CHOICES, max_length=100, blank=True, null=True
    )
    product_name = models.CharField(max_length=100, db_index=True, blank=True, null=True)
    product_weight = models.CharField(max_length=100, blank=True, null=True)
    is_negotiable = models.BooleanField(default=False)
    notice_period_days = models.CharField(max_length=2, blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
    cost = models.DecimalField(default=0, decimal_places=2, max_digits=50)
    description = models.TextField(blank=True, null=True)
    job_created_at = models.DateTimeField(auto_now_add=True, editable=False)
    job_updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'ads'
        ordering = ['-id']

    def __str__(self):
        return f'{self.service_type}'
