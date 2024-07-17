from django.db import models

# Create your models here.

class branchModel(models.Model):
    Branch_ID=models.IntegerField(primary_key=True)
    Branch_Name=models.CharField(max_length=50)
    Branch_HOD=models.CharField(max_length=50)
