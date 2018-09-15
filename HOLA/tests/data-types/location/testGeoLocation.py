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

from location.GeoLocation import GeoLocation
from location.GeoLocationJSONDecoder import decodeGeoLocation
from DataTypeJSONEncoder import DataTypeJSONEncoder


class GeoLocationTestCase(TestCase):
    def testGeoLocationSerialization(self):
        expectedJSON="{\"latitude\": 12309.01, \"longitude\": 123.12}"
        geoLocation=GeoLocation(12309.01,123.12)
        serialisedJSON=json.dumps(geoLocation,cls=DataTypeJSONEncoder)   

        if jsoncompare.are_same(expectedJSON, serialisedJSON)[0]:
            assert True
        else:
            print("expected       :",expectedJSON)
            print("serialised-form:",serialisedJSON) 
            assert False


    def testCorrectGeoLocationDeSerialization(self):
        inputJSON="{\"latitude\": 12309.01, \"longitude\": 123.12}"
        try:
            geoLocation=json.loads(inputJSON,object_hook=decodeGeoLocation)
            assert True
        except Exception:
            assert False


    def testIncorrectLatitude(self):
        inputJSON="{\"latitudes\": 12309.01, \"longitude\": 123.12}"
        try:
            geoLocation=json.loads(inputJSON,object_hook=decodeGeoLocation)
            assert False
        except Exception:
            assert True

    def testIncorrectLongitude(self):
        inputJSON="{\"latitude\": 12309.01, \"longitudes\": 123.12}"
        try:
            geoLocation=json.loads(inputJSON,object_hook=decodeGeoLocation)
            assert False
        except Exception:
            assert True
    def testIncorrectTypeLatitude(self):
        inputJSON="{\"latitude\": \"12309.01\", \"longitude\": 123.12}"
        try:
            geoLocation=json.loads(inputJSON,object_hook=decodeGeoLocation)
            assert False
        except Exception:
            assert True


    def testIncorrectTypeLongitude(self):
        inputJSON="{\"latitude\": \"12309.01\",\"longitude\": 123}"
        try:
            geoLocation=json.loads(inputJSON,object_hook=decodeGeoLocation)
            assert False
        except Exception:
            assert True