from rest_framework import serializers
import os
import sys
curr_path=os.path.dirname(__file__)
lib_path =os.path.abspath(os.path.join(curr_path,'..','location'))
sys.path.append(lib_path)
from GeoLocationSerializer import GeoLocationSerializer

# lib_path =os.path.abspath(os.path.join(curr_path,'..','..','..'))
# sys.path.append(lib_path)

# from datatypes.location.GeoLocation import GeoLocation
# from datatypes.car.CarStatus import CarStatus



#todo not yet complete
class CarStatusSerializer(serializers.Serializer):
    geoLocation = GeoLocationSerializer()
    carAvailability = serializers.CharField(max_length=100)

