from django.contrib import admin
from about.models import About
class AboutAdmin(admin.ModelAdmin):
    list_display=('about_title','about_des','aboutDoc_name','aboutDoc_specialization')



admin.site.register(About,AboutAdmin)
# Register your models here.
