from django.shortcuts import render
from .form import courseForm
from .models import courseModel
from branch_data.models import branchModel
from branch_data.forms import branchForm

# Create your views here.

def show_course(r):
    obj = courseModel.objects.all()
    obj1= branchModel.objects.all()

    return render(r, "courses.html", {'obj': obj,'obj1':obj1})
    # return render(r, "course_data/show_course.html", {'obj': obj,'obj1':obj1})



def course_details(r):
    form = courseForm
    if r.method=='POST':
        form=courseForm(r.POST)
        if form.is_valid():
            form.save(commit=True)
    else:
        form = courseForm
    return render(r,"course_data/course_details.html",{'form':form})