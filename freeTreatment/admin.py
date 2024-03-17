from django.contrib import admin
from freeTreatment.models import freeTreatment
class freeTreatmentAdmin(admin.ModelAdmin):
    list_display=('name_free','phone_free','treatment_free')



admin.site.register(freeTreatment,freeTreatmentAdmin)
# Register your models here.
