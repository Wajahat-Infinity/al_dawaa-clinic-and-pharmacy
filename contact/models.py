from django.db import models

class Contact(models.Model):
    contact_name=models.CharField(max_length=50)
    contact_email=models.CharField(max_length=50)
    contact_message=models.TextField(max_length=1000)

