from rest_framework import serializers
import os
import sys
curr_path=os.path.dirname(__file__)
lib_path =os.path.abspath(os.path.join(curr_path,'..','location'))
sys.path.append(lib_path)
from GeoLocationSerializer import GeoLocationSerializer


# tripId,finishLocation,paymentMode

class CompleteTripTransactionInputSerializer(serializers.Serializer):
    tripId = serializers.CharField(max_length=100)
    finishLocation = GeoLocationSerializer()
    paymentMode = serializers.CharField(max_length=100)
    rating = serializers.FloatField()
    feedback = serializers.CharField(max_length=100)

