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

from datatypes.location.GeoLocation import GeoLocation
from serializers.location.GeoLocationSerializer import GeoLocationSerializer




class GeoLocationTestCase(TestCase):
    def testGeoLocationSerialization(self):
        expectedJSON="{\'latitude\': 121.2, \'longitude\': 22.2}"
        geoLocation=GeoLocation(121.2,22.2)
        serializer = GeoLocationSerializer(geoLocation)
        serialisedJSON = str(serializer.data)

        if jsoncompare.are_same(expectedJSON, serialisedJSON)[0]:
            assert True
        else:
            print(" expected-form   : ",expectedJSON)
            print(" serialised-form : ",serialisedJSON) 
            assert False


    def testGeoLocationDeSerialization(self):
        inputJSONdict={"latitude": 12309.01, "longitude": 123.12}
        #now for deserializing first do the following
        inputJSONcontent = JSONRenderer().render(inputJSONdict)
        stream=BytesIO(inputJSONcontent)
        inputJSON=JSONParser().parse(stream)
        serializer = GeoLocationSerializer(data=inputJSON)
        if(serializer.is_valid()):
            assert True
        else:
            assert False

