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

from datatypes.trip.CompleteTripTransactionInput import CompleteTripTransactionInput
from datatypes.location.GeoLocation import GeoLocation
from datatypes.trip.Trip import PaymentMode
from serializers.trip.CompleteTripTransactionInputSerializer import CompleteTripTransactionInputSerializer


# tripId,finishLocation,paymentMode
class CompleteTripTransactionInputTestCase(TestCase):
    def testCompleteTripTransactionInputSerialization(self):
        expectedJSON="{\"tripId\": \"TRIP_ID_1\", \"finishLocation\": {\"latitude\": 123.1, \"longitude\": 234.1}, \"paymentMode\": \"PAYTM_PAYMENT\", \"rating\": 1.3, \"feedback\": \"Great guy!\"}"#4
        finishLocation = GeoLocation(123.1,234.1)
        completetripinp=CompleteTripTransactionInput("TRIP_ID_1",finishLocation,4,1.3,"Great guy!")
        print("completetripinp",str(completetripinp))
        serializer = CompleteTripTransactionInputSerializer(completetripinp)
        serialisedJSON=json.dumps(serializer.data)
        # serialisedJSON=str(serializer.data)
        if jsoncompare.are_same(expectedJSON, serialisedJSON)[0]:
            assert True
        else:
            print()
            print("expected       :",expectedJSON)
            print("serialised-form:",serialisedJSON) 
            assert False

    def testCompleteTripTransactionInputDeSerialization(self):
        inputJSONdict={'tripId': 'TRIP_ID_1', 'finishLocation':{'latitude':123.1,'longitude':234.1}, 'paymentMode':'PAYTM_PAYMENT', 'rating':1.2, 'feedback':'great guy!'}
        #now for deserializing first do the following
        inputJSONcontent = JSONRenderer().render(inputJSONdict)
        stream=BytesIO(inputJSONcontent)
        inputJSON=JSONParser().parse(stream)
        serializer = CompleteTripTransactionInputSerializer(data=inputJSON)
        if(serializer.is_valid()):
            # print(serializer.validated_data)
            assert True
        else:
            assert False
