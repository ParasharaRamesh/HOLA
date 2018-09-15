from django.test import TestCase

#include the following lines for jsoncompare python 3 compatability
from jsoncompare import jsoncompare
jsoncompare.long=int
jsoncompare.unicode=str
jsoncompare.xrange=range

import json
import os
import sys
curr_path=os.path.dirname(__file__)
# print("currpath is ",curr_path)
lib_path = os.path.abspath(os.path.join(curr_path, '..', '..','..','..','data-types'))
# print("lib path is ",lib_path)
sys.path.append(lib_path)

from car.Car import Car
from DataTypeJSONEncoder import *


class CarTestCase(TestCase):
    def testCarSerialization(self):
        expectedJSON="{\"carId\": \"CAR_ID_1\", \"carType\": \"CAR_TYPE_HATCHBACK\", \"carModel\": \"TOYOTA ETIOS\", \"carLicense\": \"KA03 3122\"}"
        car=Car(carId="CAR_ID_1",carType="CAR_TYPE_HATCHBACK",carModel="TOYOTA ETIOS",carLicense="KA03 3122")
        serialisedJSON=json.dumps(car,cls=DataTypeJSONEncoder)   

        if jsoncompare.are_same(expectedJSON, serialisedJSON)[0]:
            assert True
        else:
            print("expected       :",expectedJSON)
            print("serialised-form:",serialisedJSON) 
            assert False


