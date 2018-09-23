from rest_framework import serializers
import os
import sys
curr_path=os.path.dirname(__file__)
lib_path =os.path.abspath(os.path.join(curr_path,'..','trip'))
sys.path.append(lib_path)
from TripSerializer import TripSerializer


# scheduleTripTransactionStatus,trip

class ScheduleTripTransactionResultSerializer(serializers.Serializer):
    scheduleTripTransactionStatus = serializers.CharField(max_length=100)
    trip = TripSerializer()

