from django.contrib.gis import admin
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget

from .models import CarDetailsTable, CarStatusTable, DriverDetailsTable, TripTable, RatingTable


class GoogleMapAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }


class CarDetailsTableAdmin(GoogleMapAdmin):
    list_display = ("carId", "carType", "carModel", "carLicense")


class CarStatusTableAdmin(GoogleMapAdmin):
    list_display = ("carId_id", "carAvailability", "geoLocation")


class DriverStatusTableAdmin(GoogleMapAdmin):
    list_display = ("driverId", "carId_id", "name", "phone")


class TripTableAdmin(GoogleMapAdmin):
    list_display = (
        "tripId", "carId_id", "customerId_id", "driverId_id", "startTimeInEpochs", "endTimeInEpochs", "tripPrice",
        "tripStatus", "paymentMode")


class RatingTableAdmin(GoogleMapAdmin):
    list_display = (
        "tripId", "rating", "feedback")


# Register your models here.
admin.site.register(CarDetailsTable, CarDetailsTableAdmin)
admin.site.register(CarStatusTable, CarStatusTableAdmin)
admin.site.register(DriverDetailsTable, DriverStatusTableAdmin)
admin.site.register(TripTable, TripTableAdmin)
admin.site.register(RatingTable, RatingTableAdmin)
