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

from car.CarStatus import CarStatus
from location.GeoLocation import GeoLocation
from DataTypeJSONEncoder import *


class CarStatusTestCase(TestCase):
    def testCarStatusSerialization(self):
        expectedJSON="{\"geoLocation\": {\"latitude\": 12.908486, \"longitude\": 45.908486}, \"carAvailability\": \"CAR_OFF_DUTY\"}"

        geoLocation=GeoLocation(12.908486,45.908486)
        carStatus=CarStatus(geoLocation,"CAR_OFF_DUTY")
        serialisedJSON=json.dumps(carStatus,cls=DataTypeJSONEncoder)  

        if jsoncompare.are_same(expectedJSON, serialisedJSON)[0]:
            assert True
        else:
            print("expected       :",expectedJSON)
            print("serialised-form:",serialisedJSON) 
            # print("difference     :",diff(expectedJSON,serialisedJSON))
            assert False


