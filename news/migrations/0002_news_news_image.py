# Generated by Django 5.0.1 on 2024-03-14 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_image',
            field=models.FileField(default=None, null=True, unique=True, upload_to='news/'),
        ),
    ]
