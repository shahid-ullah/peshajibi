from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import AccountsModel


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = AccountsModel
        fields = ('email',)


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = AccountsModel
        fields = ('email',)
