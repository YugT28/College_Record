from django.shortcuts import render
from .models import enquiryModel
from .form import enquiryForm

# Create your views here.

def show_enquiryform(r):
    form=enquiryForm
    if r.method=='POST':
        form=enquiryForm(r.POST)
        if form.is_valid():
            form.save()
    else:
        form=enquiryForm
    return render(r,"enquiry_data/show_enquiryForm.html",{'form':form})