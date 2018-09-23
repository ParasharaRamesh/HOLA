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

from datatypes.estimate.EstimateForCarType import EstimateForCarType
from serializers.estimate.EstimateForCarTypeSerializer import EstimateForCarTypeSerializer


class EstimateForCarTypeTestCase(TestCase):
    def testEstimateForCarTypeSerialization(self):
        expectedJSON="{\'carType\': \'CAR_TYPE_HATCHBACK\', \'tripPrice\': 129.0}"
        estimate=EstimateForCarType(2,129.0)
        serializer = EstimateForCarTypeSerializer(estimate)
        serialisedJSON=str(serializer.data)
        if jsoncompare.are_same(expectedJSON, serialisedJSON)[0]:
            assert True
        else:
            print("expected       :",expectedJSON)
            print("serialised-form:",serialisedJSON) 
            assert False

    def testEstimateForCarTypeDeSerialization(self):
        inputJSONdict={'carType': 'CAR_TYPE_HATCHBACK','tripPrice':129.2}
        #now for deserializing first do the following
        inputJSONcontent = JSONRenderer().render(inputJSONdict)
        stream=BytesIO(inputJSONcontent)
        inputJSON=JSONParser().parse(stream)
        serializer = EstimateForCarTypeSerializer(data=inputJSON)
        if(serializer.is_valid()):
            assert True
        else:
            assert False


