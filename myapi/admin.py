from django.contrib import admin
from .models import Driver, Vehicle


class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'created_at', 'updated_at')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('id', 'first_name', 'last_name')


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'driver', 'make', 'plate_number', 'created_at', 'updated_at')
    list_display_links = ('id', 'model')
    search_fields = ('id', 'driver', 'model', 'plate_number', 'make')


admin.site.register(Driver, DriverAdmin)
admin.site.register(Vehicle, VehicleAdmin)