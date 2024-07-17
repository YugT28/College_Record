from django.db import models


# Create your models here.
class courseModel(models.Model):
    course_ID=models.IntegerField(primary_key=True,default=0)
    course_Name=models.CharField(max_length=30)
    branch_ID = models.IntegerField(default=0)
    course_Details=models.CharField(max_length=1000,default='NULL')
    Branch_Name=models.CharField(max_length=45)
    class Meta:
        managed = False