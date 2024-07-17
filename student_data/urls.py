from student_data import views
from django.urls import path


urlpatterns=[
    path('student_name/',views.student_name),
    path('student_details/',views.student_details),
    path('show_student/', views.show_student)

]