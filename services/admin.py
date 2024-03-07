from django.contrib import admin
from services.models import services
class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_des')



admin.site.register(services,ServiceAdmin)
# Register your models here.
