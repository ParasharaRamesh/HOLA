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

from datatypes.customer.Customer import Customer
from serializers.customer.CustomerSerializer import CustomerSerializer



class CustomerTestCase(TestCase):
    def testCarSerialization(self):
        expectedJSON="{\'customerId\': \'CUSTOMER_ID_1\', \'name\': \'Aparajit\', \'email\': \'apla@gmail.com\', \'phone\': \'9341217838\', 'pastSevenDaysRideCount': 0}"
        customer=Customer("CUSTOMER_ID_1","Aparajit","apla@gmail.com","9341217838")
        serializer = CustomerSerializer(customer)
        serialisedJSON=str(serializer.data)
        if jsoncompare.are_same(expectedJSON, serialisedJSON)[0]:
            assert True
        else:
            print()
            print("expected       :",expectedJSON)
            print("serialised-form:",serialisedJSON) 
            assert False

    def testCarDeSerialization(self):
        inputJSONdict={'customerId': 'CUSTOMER_ID_1', 'name': 'Aparajit', 'email': 'apla@gmail.com', 'phone': '9341217838','pastSevenDaysRideCount':12}
        #now for deserializing first do the following
        inputJSONcontent = JSONRenderer().render(inputJSONdict)
        stream=BytesIO(inputJSONcontent)
        inputJSON=JSONParser().parse(stream)
        serializer = CustomerSerializer(data=inputJSON)
        if(serializer.is_valid()):
            assert True
        else:
            assert False
