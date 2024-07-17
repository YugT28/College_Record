from django import forms
from .models import student_detail

class student_detailsForm(forms.ModelForm):
    class Meta:
        model=student_detail
        fields='__all__'