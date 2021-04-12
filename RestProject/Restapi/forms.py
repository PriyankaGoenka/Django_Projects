from django.forms import ModelForm
from django.core import validators
from .models import login
from django import forms

class SignIn(forms.ModelForm):
    class Meta:
        model=login
        fields="__all__"

