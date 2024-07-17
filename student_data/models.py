from django.db import models

class student_detail(models.Model):
    Student_ID = models.IntegerField(primary_key=True)
    Student_Name = models.CharField(max_length=50)
    Student_DOB  = models.DateTimeField()
    Student_Branch = models.CharField(max_length=50)
    Student_Year = models.IntegerField()



