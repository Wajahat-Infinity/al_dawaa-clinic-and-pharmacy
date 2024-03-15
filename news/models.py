from django.db import models
from tinymce.models import HTMLField
class News(models.Model):
    news_image=models.FileField(upload_to="news/",null=True,default=None,unique=True)
    news_title=models.CharField(max_length=50)
    news_details=HTMLField()
# Create your models here.
