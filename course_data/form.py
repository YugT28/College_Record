from .models import courseModel
from django import forms

class courseForm(forms.ModelForm):
    class Meta:
        model=courseModel
        fields='__all__'
