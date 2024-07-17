from django.db import models

# Create your models here.
class enquiryModel(models.Model):
    Email_ID=models.EmailField()
    Enquiry=models.CharField(max_length=255)
