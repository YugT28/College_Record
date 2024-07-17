from django import forms
from .models import branchModel

class branchForm(forms.ModelForm):
    class Meta:
        model=branchModel
        fields="__all__"

