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

from datatypes.car.CarDriver import CarDriver
from serializers.car.CarDriverSerializer import CarDriverSerializer



class CarDriverTestCase(TestCase):
    def testCarDriverSerialization(self):
        expectedJSON="{\'driverId\': \'driver_id_11\', \'name\': \'MANJUNATH\', \'phone\': \'9898712312\', \'rating\': 3.0, \'feedbacks\': [\'Great driver!\']}"
        carDriver=CarDriver("driver_id_11","MANJUNATH","9898712312","Great driver!")
        print("Cardriver",str(carDriver))
        # carDriver.driverId="driver_id_11"
        # carDriver.name="MANJUNATH"
        # carDriver.phone="9898712312"
        carDriver.rating=3.0
        # carDriver.feedbacks='Great driver!'#this line is like feedbacks.push(feedback)
        serializer = CarDriverSerializer(carDriver)
        serialisedJSON=str(serializer.data)

        if jsoncompare.are_same(expectedJSON, serialisedJSON)[0]:
            assert True
        else:
            print("expected       :",expectedJSON)
            print("serialised-form:",serialisedJSON) 
            # print("difference     :",diff(expectedJSON,serialisedJSON))
            assert False

    def testCarDriverDeSerialization(self):
        inputJSONdict={'driverId': 'driver_id_11','name':'MANJUNATH','phone':'9898712312','rating':1.3,'feedbacks':['Great Guy!','Extremely well behaved and kind!']}
        #now for deserializing first do the following
        inputJSONcontent = JSONRenderer().render(inputJSONdict)
        stream=BytesIO(inputJSONcontent)
        inputJSON=JSONParser().parse(stream)
        serializer = CarDriverSerializer(data=inputJSON)
        if(serializer.is_valid()):
            assert True
        else:
            assert False
