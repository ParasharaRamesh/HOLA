from django.test import TestCase


#include the following lines for jsoncompare python 3 compatability
from jsoncompare import jsoncompare
jsoncompare.long=int
jsoncompare.unicode=str
jsoncompare.xrange=range
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO

import json
import os
import sys


curr_path=os.path.dirname(__file__)
lib_path =os.path.abspath(os.path.join(curr_path,'..','..','..'))
sys.path.append(lib_path)

from datatypes.trip.ScheduleTripTransactionResult import ScheduleTripTransactionResult
from datatypes.trip.Trip import Trip
from datatypes.location.GeoLocation import GeoLocation
from serializers.trip.ScheduleTripTransactionResultSerializer import ScheduleTripTransactionResultSerializer


# scheduleTripTransactionStatus,trip
class ScheduleTripTransactionResultTestCase(TestCase):
    def testScheduleTripTransactionResultSerialization(self):
        expectedJSON="{\"scheduleTripTransactionStatus\": \"UNKNOWN\", \"trip\": {\"tripId\": \"TRIP_ID_1\", \"carId\": \"CAR_ID_1\", \"driverId\": \"DRIVER_ID_1\", \
\"sourceLocation\": {\"latitude\": 123.1, \"longitude\": 234.1}, \"destinationLocation\": {\"latitude\": 123.1, \"longitude\": 234.1}, \
\"startTimeInEpochs\": 123123, \"endTimeInEpochs\": 423234, \"tripPrice\": 123.13, \
\"tripStatus\": \"TRIP_STATUS_COMPLETED\", \"paymentMode\": \"PAYTM_PAYMENT\"}}"

        sourceLocation = GeoLocation(123.1,234.1)
        destinationLocation = GeoLocation(123.1,234.1)

        trip=Trip("TRIP_ID_1","CAR_ID_1","DRIVER_ID_1",sourceLocation,destinationLocation,123123,423234,123.13,4,4)

        scheduletripres=ScheduleTripTransactionResult(1,trip)
        # completetripres.completeTripTransactionStatus=1
        # completetripres.trip=trip

        serializer = ScheduleTripTransactionResultSerializer(scheduletripres)
        serialisedJSON=json.dumps(serializer.data)
        # serialisedJSON=str(serializer.data)
        if jsoncompare.are_same(expectedJSON, serialisedJSON)[0]:
            assert True
        else:
            print()
            print("expected       :",expectedJSON)
            print("serialised-form:",serialisedJSON) 
            assert False

    def testScheduleTripTransactionResultDeSerialization(self):
        inputJSONdict={'scheduleTripTransactionStatus':'UNKNOWN','trip':{'tripId': 'TRIP_ID_1', 'carId': 'CAR_ID_1', 'driverId':'DRIVER_ID_1',\
                        'sourceLocation':{'latitude':123.1,'longitude':234.1},'destinationLocation':{'latitude':123.1,'longitude':234.1},\
                        'startTimeInEpochs':123123,'endTimeInEpochs':423234,'tripPrice':123.13,\
                        'tripStatus':'TRIP_STATUS_COMPLETED', 'paymentMode':'PAYTM_PAYMENT'\
                        }}
        #now for deserializing first do the following
        inputJSONcontent = JSONRenderer().render(inputJSONdict)
        stream=BytesIO(inputJSONcontent)
        inputJSON=JSONParser().parse(stream)
        serializer = ScheduleTripTransactionResultSerializer(data=inputJSON)
        if(serializer.is_valid()):
            # print(serializer.validated_data)
            assert True
        else:
            assert False
