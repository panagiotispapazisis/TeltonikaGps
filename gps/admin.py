from django.contrib import admin
from .models import GpsData
# Register your models here.

@admin.register(GpsData)
class GpsDataAdmin(admin.ModelAdmin):
    list_display = ['message', 'timestamp']
    
