from django.db import models
from tinymce.models import HTMLField

class About(models.Model):
    about_title=models.CharField(max_length=50)
    about_des=HTMLField()
    aboutDoc_name=models.CharField(max_length=50)
    aboutDoc_specialization=models.CharField(max_length=50)



# Create your models here.
