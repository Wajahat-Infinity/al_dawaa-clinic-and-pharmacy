from django.db import models
from tinymce.models import HTMLField

class freeTreatment(models.Model):
    name_free=models.CharField(max_length=50)
    phone_free=models.CharField(max_length=50)
    treatment_free=models.CharField(max_length=50)


# Create your models here.
