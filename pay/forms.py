from django import forms
from django.forms import ModelForm
from .models import *


class OrderForm(ModelForm):
    # cost = forms.CharField(required=False)
    # abon = forms.CharField(required=False)
    # qty = forms.CharField(required=False)
    # kid_age = forms.CharField(required=False)
    class Meta:
        model = OrderModel
        fields = ['kids_name', 'birth_date', 'cost', 'abon', 'qty', 'name', 'email', 'tel', 'branches']

    def __str__(self):
        return self.branches
