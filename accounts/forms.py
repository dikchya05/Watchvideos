from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.USER_ROLES)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']
