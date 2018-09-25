from django.db import models
import os,sys
# import CarType
curr_path=os.path.dirname(__file__)
lib_path = os.path.abspath(os.path.join(curr_path,'datatypes','car'))
sys.path.append(lib_path)
from Car import CarType
from CarStatus import CarAvailabilityStatus
from GeoLocation import GeoLocation
# from datatypes.car.CarStatus import CarAvailabilityStatus
# import Car.CarAvailabilityStatus
# from datatypes.location import GeoLocation
# import Geolocation.GeoLocation

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    pastSevenDaysRideCount=models.IntegerField()

class CarDetails(models.Model):
    carType=models.CharField(max_length=30,choices=[(tag,tag.value) for tag in CarType])
    # carAvailability=models.CharField(max_length=30,choices=[(tag,tag.value) for tag in CarAvailabilityStatus])
    # geoLocation=models.Field(GeoLocation)
class DriverDetails(models.Model):
    carId=models.OneToOneField(CarDetails,on_delete=models.CASCADE,related_name="carId")
    