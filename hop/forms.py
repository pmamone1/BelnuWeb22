from django import forms
from .models import Hop
#from django.forms import *
from django.contrib.admin.widgets import AdminDateWidget

class DateInput(forms.DateInput):
    input_type='date'
    format=('%Y-%m-%d')

class HopForm(forms.ModelForm):
    class Meta:
        model = Hop
        fields = '__all__'
        fecha = forms.DateField(
                    localize=True,
                    widget=forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date', 'class': 'form-control'}),
)
        