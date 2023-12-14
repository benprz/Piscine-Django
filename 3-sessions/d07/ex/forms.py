from django import forms
from .models import User

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password2', max_length=100, widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError(
                "Passwords do not match"
            )
        return cleaned_data
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "Username already exists"
            )
        return username

    def save(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get("password")
        user = User.objects.create_user(username, password)
        return user