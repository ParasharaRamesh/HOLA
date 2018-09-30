from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomerTable)
admin.site.register(DriverDetailsTable)
admin.site.register(CarDetailsTable)
admin.site.register(CarStatusTable)
admin.site.register(TripTable)