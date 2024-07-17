from django import forms
from .models import faculty_detail

class faculty_detailsForm(forms.ModelForm):
    class Meta:
        model=faculty_detail
        fields='__all__'