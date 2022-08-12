
from django import forms
from django.forms import ModelForm

from .models import *
 



class ShopcartForm(forms.ModelForm):
    class Meta:
        model = Shopcart
        fields = ['quantity']