from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def branch_name(r):
    return HttpResponse("<h1>BRACH NAME</h1>")

