# Generated by Django 5.0.1 on 2024-04-29 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='aboutDoc_name',
        ),
        migrations.RemoveField(
            model_name='about',
            name='aboutDoc_specialization',
        ),
    ]