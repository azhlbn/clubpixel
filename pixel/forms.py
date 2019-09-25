from django import forms
from django.forms import ModelForm
from .models import *
from signup.models import SignupModel


class BonusForm(ModelForm):
    name = forms.CharField(max_length=50)
    tel = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    kids_name = forms.CharField(max_length=50)
    branches = forms.CharField(max_length=200)
    message = forms.CharField(max_length=70)
    class Meta:
        model = BonusModel
        fields = ['name', 'tel', 'email', 'kids_name', 'message', 'branches']


class SignupForm(ModelForm):
    name = forms.CharField(required=True)
    tel = forms.CharField(required=True)
    email = forms.CharField(required=True)
    kid_name = forms.CharField(required=False)
    kid_age = forms.CharField(required=False)
    branches = forms.CharField(max_length=200, required=False)
    service = forms.CharField(max_length=200, required=False)
    class Meta:
        model = SignupModel
        fields = ['name', 'tel', 'email', 'kid_name', 'kid_age', 'branches', 'service']

    def __str__(self):
        return self.branches
