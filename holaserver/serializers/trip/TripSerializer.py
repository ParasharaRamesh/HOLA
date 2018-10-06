from rest_framework import serializers
import os
import sys
curr_path=os.path.dirname(__file__)
lib_path =os.path.abspath(os.path.join(curr_path,'..','location'))
sys.path.append(lib_path)
from GeoLocationSerializer import GeoLocationSerializer




class TripSerializer(serializers.Serializer):
    tripId = serializers.CharField(max_length=100)
    carId = serializers.CharField(max_length=100)
    driverId = serializers.CharField(max_length=100)
    customerId = serializers.CharField(max_length=100)
    sourceLocation = GeoLocationSerializer()
    destinationLocation = GeoLocationSerializer()
    startTimeInEpochs = serializers.IntegerField()
    endTimeInEpochs = serializers.IntegerField()
    tripPrice = serializers.FloatField()
    tripStatus = serializers.CharField(max_length=100)
    paymentMode = serializers.CharField(max_length=100)
    rating = serializers.FloatField()
    feedback = serializers.CharField(max_length=100)


