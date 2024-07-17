from django.shortcuts import render
from django.http import HttpResponse
from .form import student_detailsForm
from .models import student_detail
# Create your views here.


def student_name(r):
    return HttpResponse("<h1>Student NAME</h1>")

def student_details(r):
    form = student_detailsForm
    if r.method=='POST':
        form=student_detailsForm(r.POST)
        if form.is_valid():
            form.save(commit=True)
    else:
        form = student_detailsForm
    return render(r,"student_data/student_details.html",{'form':form})

def show_student(r):
    obj=student_detail.objects.all()
    return render(r,'student_data/show_student.html',{'obj':obj})
# Create your views here.
