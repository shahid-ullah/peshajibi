from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AccountChangeForm, AccountCreationForm
from .models import AccountsModel, DivisionUserProfileModel, GuestUserProfileModel, UserTypeModel


class AccountsAdmin(UserAdmin):
    add_form = AccountCreationForm
    form = AccountChangeForm
    model = AccountsModel
    list_display = (
        'mobile',
        'is_staff',
        'is_active',
    )
    list_filter = (
        'email',
        'is_staff',
        'is_active',
    )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(AccountsModel, AccountsAdmin)
admin.site.register(UserTypeModel)
admin.site.register(GuestUserProfileModel)
admin.site.register(DivisionUserProfileModel)
