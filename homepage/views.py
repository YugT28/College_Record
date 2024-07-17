from django.shortcuts import render

# Create your views here.

def show_homepage(r):
    return render(r,"index.html")

