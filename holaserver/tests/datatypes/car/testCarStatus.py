from django.test import TestCase


#include the following lines for jsoncompare python 3 compatability
from jsoncompare import jsoncompare
import json
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

from datatypes.car.CarStatus import CarStatus
from serializers.car.CarStatusSerializer import CarStatusSerializer
# from datatypes.location.GeoLocation import GeoLocation
lib_path =os.path.abspath(os.path.join(lib_path,'..','..','..','datatypes','location'))
sys.path.append(lib_path)
from GeoLocation import GeoLocation

from copy import deepcopy

class CarStatusTestCase(TestCase):
    def testCarStatusSerialization(self):
        expectedJSON="{\"carId\": \"CAR_ID_1\", \"geoLocation\": {\"latitude\": 12.91, \"longitude\": 45.92}, \"carAvailability\": \"CAR_OFF_DUTY\"}"
        geoLocation=GeoLocation(12.91,45.92)
        carStatus=CarStatus("CAR_ID_1",geoLocation,2)
        # carStatus.geoLocation=geoLocation
        # carStatus.carAvailability=2
        serializer = CarStatusSerializer(carStatus)
        # print(serializer.data)
        serialisedJSON = json.dumps(serializer.data) 

        if jsoncompare.are_same(expectedJSON, serialisedJSON)[0]:
            assert True
        else:
            print("expected       :",expectedJSON)
            print("serialised-form:",serialisedJSON) 
            # print("difference     :",diff(expectedJSON,serialisedJSON))
            assert False

    def testCarStatusDeSerialization(self):
        inputJSONdict={"carId":"CAR_ID_1" ,"geoLocation":{"latitude":12.23,"longitude":23.22},"carAvailability": "CAR_OFF_DUTY"}
        #now for deserializing first do the following
        inputJSONcontent = JSONRenderer().render(inputJSONdict)
        stream=BytesIO(inputJSONcontent)
        inputJSON=JSONParser().parse(stream)
        serializer = CarStatusSerializer(data=inputJSON)
        if(serializer.is_valid()):
            # print(serializer.validated_data)
            assert True
        else:
            assert False


