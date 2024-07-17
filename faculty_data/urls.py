from faculty_data import views
from django.urls import path


urlpatterns=[
    # path('faculty_name/',views.student_name),
    path('faculty_details/',views.faculty_details),
    path('show_faculty/', views.show_faculty)

]