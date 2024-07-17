from django.db import models

# Create your models here.

class faculty_detail(models.Model):
    Faculty_ID = models.IntegerField(primary_key=True)
    Faculty_Name = models.CharField(max_length=50)
    Faculty_Date_of_joining  = models.DateTimeField()
    Faculty_Branch = models.CharField(max_length=50)
