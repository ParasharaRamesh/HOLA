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

from datatypes.car.Car import Car
from serializers.car.CarSerializer import CarSerializer






class CarTestCase(TestCase):
    def testCarSerialization(self):
        expectedJSON="{\'carId\': \'CAR_ID_1\', \'carType\': \'CAR_TYPE_HATCHBACK\', \'carModel\': \'TOYOTA ETIOS\', \'carLicense\': \'KA03 3122\'}"
        car=Car("CAR_ID_1",2,"TOYOTA ETIOS","KA03 3122")
        print("Car",str(car))
        # car.carId="CAR_ID_1"
        # car.carType=2
        # car.carModel="TOYOTA ETIOS"
        # car.carLicense="KA03 3122"
        serializer = CarSerializer(car)
        serialisedJSON=str(serializer.data)
        if jsoncompare.are_same(expectedJSON, serialisedJSON)[0]:
            assert True
        else:
            print("expected       :",expectedJSON)
            print("serialised-form:",serialisedJSON) 
            assert False

    def testCarDeSerialization(self):
        inputJSONdict={'carId': 'CAR_ID_1', 'carType': 'CAR_TYPE_HATCHBACK', 'carModel': 'TOYOTA ETIOS', 'carLicense': 'KA03 3122'}
        #now for deserializing first do the following
        inputJSONcontent = JSONRenderer().render(inputJSONdict)
        stream=BytesIO(inputJSONcontent)
        inputJSON=JSONParser().parse(stream)
        serializer = CarSerializer(data=inputJSON)
        if(serializer.is_valid()):
            assert True
        else:
            assert False

      


