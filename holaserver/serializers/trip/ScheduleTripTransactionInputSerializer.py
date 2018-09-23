from rest_framework import serializers
import os
import sys
curr_path=os.path.dirname(__file__)
lib_path =os.path.abspath(os.path.join(curr_path,'..','location'))
sys.path.append(lib_path)
from GeoLocationSerializer import GeoLocationSerializer


# carType,tripPrice,sourceLocation,destinationLocation

class ScheduleTripTransactionInputSerializer(serializers.Serializer):
    carType = serializers.CharField(max_length=100)
    tripPrice = serializers.FloatField()
    sourceLocation = GeoLocationSerializer()
    destinationLocation = GeoLocationSerializer()


