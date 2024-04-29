from django.db import models
from tinymce.models import HTMLField

class About(models.Model):
    about_title=models.CharField(max_length=50)
    about_des=HTMLField()




# Create your models here.
