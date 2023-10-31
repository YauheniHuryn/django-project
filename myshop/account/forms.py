from django import forms
from django.contrib.auth.password_validation import validate_password

from .models import User


class RegistrationForm(forms.ModelForm):
    password_repeat = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "id": "password_repeat"}),
        validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ("username", "email", "password")
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "id": "username", "placeholder": "Username"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "id": "email", "placeholder": "E-Mail Address"}),
            "password": forms.PasswordInput(
                attrs={"class": "form-control", "id": "password", "placeholder": "Password"}
            ),
        }


