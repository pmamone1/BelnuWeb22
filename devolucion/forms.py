from django import forms
from .models import doc_belnu,doc_Nacion,ExcelFileUpload
#from django.forms import *
from django.contrib.admin.widgets import AdminDateWidget

class DateInput(forms.DateInput):
    input_type='date'
    format=('%Y-%m-%d')

class Doc_belnuForm(forms.ModelForm):
    class Meta:
        model = doc_belnu
        fields = '__all__'
        fecha = forms.DateField(
                    localize=True,
                    widget=forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date', 'class': 'form-control'}),
)
        