from django.db import models
from model_utils import Choices
import os,sys
# import CarType
curr_path=os.path.dirname(__file__)
lib_path = os.path.abspath(os.path.join(curr_path,'datatypes'))
sys.path.append(lib_path)
# print("in models",lib_path)
from car.Car import CarType
from car.CarStatus import CarAvailabilityStatus
from location.GeoLocation import GeoLocation
from trip.Trip import Trip,TripStatus,PaymentMode

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

# models are defined below
#writing explicit primary key id's as there are problems when serializing
class CustomerTable(models.Model):
    customerId=models.AutoField(primary_key=True,default=1)
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    pastSevenDaysRideCount=models.PositiveIntegerField()
    
    class Meta:
        verbose_name_plural = "CustomerTable"

class CarDetailsTable(models.Model):
    carId=models.AutoField(primary_key=True)
    carType=models.CharField(max_length=100,choices=[(tag.name,tag.value) for tag in CarType],default=str(CarType.UNKNOWN))
    carModel=models.CharField(max_length=50)
    carLicense=models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "CarDetailsTable"

class CarStatusTable(models.Model):
    carId = models.OneToOneField(CarDetailsTable,verbose_name="carId",on_delete=models.CASCADE,unique=True)
    carAvailability=models.CharField(max_length=100,choices=[(tag.name,tag.value) for tag in CarAvailabilityStatus],default=str(CarAvailabilityStatus.UNKNOWN))
    geoLocation = GeoLocationField()
    
    class Meta:
        verbose_name_plural = "CarStatusTable"

class DriverDetailsTable(models.Model):
    driverId=models.AutoField(primary_key=True,default=1)
    carId=models.OneToOneField(CarDetailsTable,verbose_name="carId",on_delete=models.CASCADE,default=1)#ie a driver can ride multiple cars and each car can be driven by multiple drivers
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    avg_rating=models.FloatField(default=0.0)#the average of all the ratings he has received so far

    class Meta:
        verbose_name_plural = "DriverDetailsTable"

class TripTable(models.Model):
    tripId=models.AutoField(primary_key=True)
    carId = models.ForeignKey(CarDetailsTable,verbose_name="carId",on_delete=models.CASCADE,null=True)
    #driver id is unique for each car
    customerId = models.ForeignKey(CustomerTable,verbose_name="customerId",on_delete=models.CASCADE,null=True)
    sourceLocation = GeoLocationField()
    destinationLocation = GeoLocationField()
    startTimeInEpochs = models.PositiveIntegerField()
    endTimeInEpochs = models.PositiveIntegerField()
    tripPrice = models.FloatField()
    tripStatus = models.CharField(max_length=100,choices=[(tag.name,tag.value) for tag in TripStatus],default=str(TripStatus.UNKNOWN))
    paymentMode = models.CharField(max_length=100,choices=[(tag.name,tag.value) for tag in TripStatus],default=str(PaymentMode.UNKNOWN))
    rating = models.FloatField(default=0.0)#pertrip which will be aggregated and averaged for that particular driverId
    feedback = models.CharField(max_length=240)#query top 5 feedbacks about the driver using this attribute

    class Meta:
        verbose_name_plural = "TripTable"