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

from datatypes.trip.ScheduleTripTransactionInput import ScheduleTripTransactionInput
from datatypes.location.GeoLocation import GeoLocation
from datatypes.car.Car import CarType
from serializers.trip.ScheduleTripTransactionInputSerializer import ScheduleTripTransactionInputSerializer



class ScheduleTripTransactionInputTestCase(TestCase):
    def testScheduleTripTransactionInputSerialization(self):
        expectedJSON="{\"carType\": \"CAR_TYPE_AUTO\", \"tripPrice\": 123.13, \
\"sourceLocation\": {\"latitude\": 123.1, \"longitude\": 234.1}, \"destinationLocation\": {\"latitude\": 123.1, \"longitude\": 234.1}}"

        sourceLocation = GeoLocation(123.1,234.1)
        destinationLocation = GeoLocation(123.1,234.1)
        scheduletripinp=ScheduleTripTransactionInput(5,123.13,sourceLocation,destinationLocation)
        print("sccheduletripinp",str(scheduletripinp))
        serializer = ScheduleTripTransactionInputSerializer(scheduletripinp)
        serialisedJSON=json.dumps(serializer.data)
        # serialisedJSON=str(serializer.data)
        if jsoncompare.are_same(expectedJSON, serialisedJSON)[0]:
            assert True
        else:
            print()
            print("expected       :",expectedJSON)
            print("serialised-form:",serialisedJSON) 
            assert False

    def testScheduleTripTransactionInputDeSerialization(self):
        inputJSONdict={'carType': 'CAR_TYPE_AUTO', 'tripPrice':123.13,\
                        'sourceLocation':{'latitude':123.1,'longitude':234.1},'destinationLocation':{'latitude':123.1,'longitude':234.1},\
                        }
        #now for deserializing first do the following
        inputJSONcontent = JSONRenderer().render(inputJSONdict)
        stream=BytesIO(inputJSONcontent)
        inputJSON=JSONParser().parse(stream)
        serializer = ScheduleTripTransactionInputSerializer(data=inputJSON)
        if(serializer.is_valid()):
            # print(serializer.validated_data)
            assert True
        else:
            assert False
