from django.db import models
from model_utils import Choices
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

# print("CAR AVAILABILITY",[(tag,tag.value) for tag in CarAvailabilityStatus])
# print("car type",[(tag,tag.value) for tag in CarType])
#custom fields
class GeoLocationField(models.Field):
    description = "A latitude,longitude pair"


    def __init__(self,help_text=("A comma-separated latitude longitude pair"),verbose_name='geoLocationField', *args,**kwargs):
        self.name="GeoLocationField",
        self.through = None
        self.help_text = help_text
        self.blank = True
        self.editable = True
        self.creates_table = False
        self.db_column = None
        self.serialize = False
        self.null = True
        self.creation_counter = models.Field.creation_counter
        models.Field.creation_counter += 1
        super(GeoLocationField, self).__init__(*args, **kwargs)
        
        
    def db_type(self, connection):
        return 'varchar(100)'


    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        else:
            args = [float(value.split(',')[0]),float(value.split(',')[1])]
            if len(args) != 2 and value is not None:
                Exception("Invalid input for a GeoLocation instance")
            return GeoLocation(*args)

    
    def to_python(self,value):
        if value in ( None,''):
            return GeoLocation()
        else:
            if isinstance(value, GeoLocation):
                return value
            else:
                args = [float(value.split(',')[0]),float(value.split(',')[1])]
                if len(args) != 2 and value is not None:
                    Exception("Invalid input for a GeoLocation instance")
                return GeoLocation(*args)
         

    def get_prep_value(self, value):
        if value is None:
            return ','.join([str(0.0),str(0.0)])
        else:
            return ','.join([str(value.latitude),str(value.longitude)])
    
    def get_internal_type(self):
        return 'CharField'
    
    def value_to_string(self, obj):
        # value = self._get_val_from_obj(obj)
        return self.get_prep_value(obj)


# Create your models here.
class CustomerTable(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    pastSevenDaysRideCount=models.IntegerField()

class CarDetailsTable(models.Model):
    carAvailability=models.CharField(max_length=100,choices=[(tag.name,tag.value) for tag in CarAvailabilityStatus],default=str(CarAvailabilityStatus.UNKNOWN))
    carType=models.CharField(max_length=100,choices=[(tag.name,tag.value) for tag in CarType],default=str(CarType.UNKNOWN))
    geoLocation = GeoLocationField()

class DriverDetailsTable(models.Model):
    carId=models.OneToOneField(CarDetailsTable,on_delete=models.CASCADE,related_name="carId")
    