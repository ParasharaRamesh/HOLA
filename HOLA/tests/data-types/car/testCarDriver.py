from django.test import TestCase

#include the following lines for jsoncompare python 3 compatability
from jsoncompare import jsoncompare
jsoncompare.long=int
jsoncompare.unicode=str
jsoncompare.xrange=range

# from jsondiff import diff

import json
import os
import sys
curr_path=os.path.dirname(__file__)
# print("currpath is ",curr_path)
lib_path = os.path.abspath(os.path.join(curr_path, '..', '..','..','..','data-types'))
# print("lib path is ",lib_path)
sys.path.append(lib_path)

from car.CarDriver import CarDriver
from DataTypeJSONEncoder import *


class CarDriverTestCase(TestCase):
    def testCarDriverSerialization(self):
        expectedJSON="{\"driverId\": \"driver_id_11\", \"name\": \"MANJUNATH\", \"phone\": \"9898712312\", \"rating\": 0.0, \"feedbacks\": []}"
        carDriver=CarDriver("driver_id_11","MANJUNATH","9898712312")
        serialisedJSON=json.dumps(carDriver,cls=DataTypeJSONEncoder)  

        if jsoncompare.are_same(expectedJSON, serialisedJSON)[0]:
            assert True
        else:
            print("expected       :",expectedJSON)
            print("serialised-form:",serialisedJSON) 
            # print("difference     :",diff(expectedJSON,serialisedJSON))
            assert False


