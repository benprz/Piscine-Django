# forms.py
from django import forms

class History(forms.Form):
    text = forms.CharField(max_length=100)