from django.contrib import admin

# Register your models here.
from gd_admin.models import Vendor_Register, Employee, GoDown

admin.site.register(Vendor_Register)
admin.site.register(Employee)
admin.site.register(GoDown)