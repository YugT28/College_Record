from django.shortcuts import render
from .form import faculty_detailsForm
from .models import faculty_detail
# Create your views here.
def faculty_details(r):
    form = faculty_detailsForm
    if r.method == 'POST':
        form = faculty_detailsForm(r.POST)
        if form.is_valid():
            form.save(commit=True)
    else:
        form = faculty_detailsForm
    return render(r, "faculty_data/faculty_details.html", {'form': form})


def show_faculty(r):
    obj = faculty_detail.objects.all()
    return render(r, 'faculty_data/show_faculty.html', {'obj': obj})