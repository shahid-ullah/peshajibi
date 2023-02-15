# Create your models here.
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import authentication

from apps.peshajibi.models import (
    CityCorporationModel,
    CityCorporationThanaModel,
    DistrictModel,
    DivisionModel,
    ProfessionModel,
    UnionModel,
    UpazilaModel,
)

from .managers import AccountManager


class UserTypeModel(models.Model):
    '''
    The Role entries are managed by the system,
    automatically created via a Django data migration.
    '''

    PESHAJIBI_USER = 1
    GUEST_USER = 2
    ROLE_CHOICES = (
        (PESHAJIBI_USER, 'peshajibi'),
        (GUEST_USER, 'guest'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    class Meta:
        db_table = "user_type"
        ordering = ['id']

    def __str__(self):
        return f'{self.id}'


class AccountsModel(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=150,
        blank=True,
        null=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
    )
    user_type = models.ManyToManyField(UserTypeModel)
    favourites = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    email = models.EmailField(_('email address'), unique=False, blank=True, null=True)
    mobile = models.CharField(_('mobile number'), max_length=100, unique=True)
    photo = models.ImageField(upload_to='accounts/', blank=True, null=True)
    latitude = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    blood_group_bng = models.CharField(max_length=10, blank=True, null=True)
    blood_group_eng = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "account"
        ordering = ['id']

    objects = AccountManager()

    def __str__(self):
        return f'{self.mobile}'


class GuestUserProfileModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='guest_profile')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "guest_user"
        ordering = ['id']

    def __str__(self):
        return f'{self.user.mobile}'


class CityCorporationUserProfileModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='city_profile')
    profession = models.ForeignKey(ProfessionModel, on_delete=models.CASCADE, blank=True, null=True)
    present_city = models.ForeignKey(
        CityCorporationModel, on_delete=models.CASCADE, related_name='current_city_users', blank=True, null=True
    )
    permanent_city = models.ForeignKey(
        CityCorporationModel, on_delete=models.CASCADE, related_name='permanent_city_users', blank=True, null=True
    )
    present_thana = models.ForeignKey(
        CityCorporationThanaModel, on_delete=models.CASCADE, related_name='current_thana_users', blank=True, null=True
    )
    permanent_thana = models.ForeignKey(
        CityCorporationThanaModel, on_delete=models.CASCADE, related_name='permanent_thana_users', blank=True, null=True
    )
    present_sector = models.CharField(max_length=100, blank=True, null=True)
    permanent_sector = models.CharField(max_length=100, blank=True, null=True)
    present_flat_no = models.CharField(max_length=100, blank=True, null=True)
    permanent_flat_no = models.CharField(max_length=100, blank=True, null=True)
    present_house_no = models.CharField(max_length=100, blank=True, null=True)
    permanent_house_no = models.CharField(max_length=100, blank=True, null=True)
    present_road_no = models.CharField(max_length=100, blank=True, null=True)
    permanent_road_no = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "city_user_profile"
        ordering = ['id']

    def __str__(self):
        return f'{self.user.mobile}'


class DivisionUserProfileModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='division_profile')
    profession = models.ForeignKey(ProfessionModel, on_delete=models.CASCADE, null=True, blank=True)
    present_division = models.ForeignKey(
        DivisionModel, on_delete=models.CASCADE, related_name='current_division_users', null=True, blank=True
    )
    permanent_division = models.ForeignKey(
        DivisionModel, on_delete=models.CASCADE, related_name='permanent_division_users', null=True, blank=True
    )
    present_district = models.ForeignKey(
        DistrictModel, on_delete=models.CASCADE, related_name='current_district_users', blank=True, null=True
    )
    permanent_district = models.ForeignKey(
        DistrictModel, on_delete=models.CASCADE, related_name='permanent_district_users', blank=True, null=True
    )
    present_upazila = models.ForeignKey(
        UpazilaModel, on_delete=models.CASCADE, related_name='current_upazila_users', blank=True, null=True
    )
    permanent_upazila = models.ForeignKey(
        UpazilaModel, on_delete=models.CASCADE, related_name='permanent_upazila_users', blank=True, null=True
    )
    present_union = models.ForeignKey(
        UnionModel, on_delete=models.CASCADE, related_name='current_union_users', blank=True, null=True
    )
    permanent_union = models.ForeignKey(
        UnionModel, on_delete=models.CASCADE, related_name='permanent_union_users', blank=True, null=True
    )
    present_ward = models.CharField(max_length=100, blank=True, null=True)
    permanent_ward = models.CharField(max_length=100, blank=True, null=True)
    present_house_no = models.CharField(max_length=100, blank=True, null=True)
    permanent_house_no = models.CharField(max_length=100, blank=True, null=True)
    present_village = models.CharField(max_length=100, blank=True, null=True)
    permanent_village = models.CharField(max_length=100, blank=True, null=True)
    present_road_no = models.CharField(max_length=100, blank=True, null=True)
    permanent_road_no = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "division_user_profile"
        ordering = ['id']

    def __str__(self):
        return f'{self.user.mobile}'


class BearerAuthentication(authentication.TokenAuthentication):
    '''
    Authorization: Bearer 956e252a-513c-48c5-92dd-bfddc364e812
    '''

    keyword = 'Bearer'
