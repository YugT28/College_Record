from .models import enquiryModel
from django import forms

class enquiryForm(forms.ModelForm):
    class Meta:
        model=enquiryModel
        fields='__all__'