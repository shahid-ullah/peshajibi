from django.db import models


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
        ordering = ['id']

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
        ordering = ['id']

    def __str__(self):
        return f'{self.name_bng} {self.name_eng}'


class JobTypeModel(models.Model):
    name_bng = models.CharField(max_length=100, blank=True, null=True)
    name_eng = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "job_type"
        ordering = ['id']

    def __str__(self):
        return f'{self.name_bng} {self.name_eng}'
