from course_data import views
from django.urls import path


urlpatterns=[
    path('course_details/',views.course_details),
    path('show_course/', views.show_course)

]