from django.contrib import admin
from doctors.models import Doctors
class DocAdmin(admin.ModelAdmin):
    list_display=('aboutDoc_name','aboutDoc_specialization','aboutDoc_image')



admin.site.register(Doctors,DocAdmin)

# Register your models here.
