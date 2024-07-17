from branch_data import views
from django.urls import path


urlpatterns=[
    path('branch_name/',views.branch_name),
]