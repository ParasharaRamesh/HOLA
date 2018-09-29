import os
import enum
import sys
curr_path=os.path.dirname(__file__)
# print("currpath is ",curr_path)
lib_path = os.path.abspath(os.path.join(curr_path, '..','..'))
# print("in trip lib path is ",lib_path)
sys.path.append(lib_path)
from datatypes.location.GeoLocation import GeoLocation

lib_path = os.path.abspath(os.path.join(curr_path, '..','trip'))
# print("in conpletetrip lib path is ",lib_path)
sys.path.append(lib_path)
import Trip

class CompleteTripTransactionInput:
    def __init__(self,tripId,finishLocation,paymentMode):
        self._tripId=tripId#strin
        if isinstance(finishLocation,GeoLocation) == True:
            self._finishLocation=finishLocation#geolocation
        else:
            Exception('The rvalue is of not of geolocation type!')

        if type(paymentMode)!=int:
            Exception("paymentMode must be an integer between 1-4")
        if paymentMode<1 or paymentMode>4:
            Exception("paymentMode must be between 1 and 4")
        self._paymentMode=str(Trip.PaymentMode(paymentMode))[12:]

    def __str__(self):
        return '%s(%s)' % (type(self).__name__,', '.join('%s=%s' % item for item in vars(self).items()))

    #getters and setters
    @property
    def tripId(self):
        return self._tripId

    @tripId.setter
    def tripId(self,tripId):
        self._tripId=tripId
    
    @property
    def finishLocation(self):
        return self._finishLocation
    
    @finishLocation.setter
    def finishLocation(self,finishLocation):
        if isinstance(finishLocation,GeoLocation) == True:
            self._finishLocation=finishLocation#geolocation
        else:
            Exception('The rvalue is of not of geolocation type!')
        
    @property
    def paymentMode(self):
        return self._paymentMode
    
    @paymentMode.setter
    def paymentMode(self,paymentMode):
        if type(paymentMode)!=int:
            Exception("paymentMode must be an integer between 1-4")
        if paymentMode<1 or paymentMode>4:
            Exception("paymentMode must be between 1 and 4")
        self._paymentMode=str(Trip.PaymentMode(paymentMode))[12:]

