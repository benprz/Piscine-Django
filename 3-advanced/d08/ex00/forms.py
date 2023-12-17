from django import forms
from django.contrib.auth.forms import (
    UsernameField,
    AuthenticationForm,
)


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput())
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                # 'class': 'form-control'
            }),
        )