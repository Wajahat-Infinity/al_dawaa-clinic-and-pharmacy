from django.db import models
from tinymce.models import HTMLField

class Doctors(models.Model):
    aboutDoc_image=models.FileField(upload_to="doctors/",null=True,default=None,unique=True)
    aboutDoc_name=models.CharField(max_length=50)
    aboutDoc_specialization=models.CharField(max_length=50)
    # aboutDoc_img=models.ImageField(upload_to='images/')


# Create your models here.
