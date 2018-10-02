import os
import enum
import sys
curr_path=os.path.dirname(__file__)
# print("currpath is ",curr_path)
lib_path = os.path.abspath(os.path.join(curr_path, '..','..'))
# print("in trip lib path is ",lib_path)
sys.path.append(lib_path)
from datatypes.location.GeoLocation import GeoLocation



class PaymentMode(enum.Enum):
    UNKNOWN=1
    CASH_PAYMENT=2
    CARD_PAYMENT=3
    PAYTM_PAYMENT=4

class TripStatus(enum.Enum):
    UNKNOWN=1
    TRIP_STATUS_SCHEDULED=2#this is used
    TRIP_STATUS_ONGOING=3#never used as we are not properly simulating
    TRIP_STATUS_COMPLETED=4#this is used
    TRIP_STATUS_CANCELLED=5#this is used

class Trip:
    def __init__(self,tripId,carId,driverId,customerId,sourceLocation,destinationLocation,startTimeInEpochs,endTimeInEpochs,tripPrice,tripStatus,paymentMode):
        self._tripId=tripId#string
        self._carId=carId#string
        self._driverId=driverId#string
        self._customerId=customerId#string
        # print("srcLoc",type(sourceLocation),isinstance(sourceLocation,GeoLocation.GeoLocation))
        if isinstance(sourceLocation,GeoLocation) == True:
            self._sourceLocation=sourceLocation
        else:
            Exception('The rvalue is of not of geolocation type!')

        if isinstance(destinationLocation,GeoLocation) == True:
            self._destinationLocation=destinationLocation
        else:
            Exception('The rvalue is of not of geolocation type!')

        self._startTimeInEpochs=startTimeInEpochs#Long
        self._endTimeInEpochs=endTimeInEpochs#Long

        if type(tripPrice)==float:
            self._tripPrice=tripPrice#float
        else:
            Exception("trip price must be a float value!")
        
        if type(tripStatus)!=int:
            Exception("tripStatus must be an integer between 1-5")
        if tripStatus<1 or tripStatus>5:
            Exception("tripStatus must be between 1 and 5")
        self._tripStatus=str(TripStatus(tripStatus))[11:]

        if type(paymentMode)!=int:
            Exception("paymentMode must be an integer between 1-4")
        if paymentMode<1 or paymentMode>4:
            Exception("paymentMode must be between 1 and 4")
        self._paymentMode=str(PaymentMode(paymentMode))[12:]

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
    def carId(self):
        return self._carId

    @carId.setter
    def carId(self,carId):
        self._carId=carId

    @property
    def driverId(self):
        return self._driverId

    @driverId.setter
    def driverId(self,driverId):
        self._driverId=driverId

    @property
    def customerId(self):
        return self._customerId

    @customerId.setter
    def customerId(self,customerId):
        self._customerId=customerId


    @property
    def sourceLocation(self):
        return self._sourceLocation

    @sourceLocation.setter
    def sourceLocation(self,sourceLocation):
        if isinstance(sourceLocation,GeoLocation) == True:
            self._sourceLocation=sourceLocation
        else:
            Exception('The rvalue is of not of geolocation type!')

    @property
    def destinationLocation(self):
        return self._destinationLocation

    @destinationLocation.setter
    def destinationLocation(self,destinationLocation):
        if isinstance(destinationLocation,GeoLocation) == True:
            self._destinationLocation=destinationLocation
        else:
            Exception('The rvalue is of not of geolocation type!')

    @property
    def startTimeInEpochs(self):
        return self._startTimeInEpochs

    @startTimeInEpochs.setter
    def startTimeInEpochs(self,startTimeInEpochs):
        self._startTimeInEpochs = startTimeInEpochs

    @property
    def endTimeInEpochs(self):
        return self._endTimeInEpochs

    @endTimeInEpochs.setter
    def endTimeInEpochs(self,endTimeInEpochs):
        self._endTimeInEpochs = endTimeInEpochs

    @property
    def tripPrice(self):
        return self._tripPrice
    
    @tripPrice.setter
    def tripPrice(self,tripPrice):
        if type(tripPrice)==float:
            self._tripPrice=tripPrice#float
        else:
            Exception("trip price must be a float value!")

    @property
    def tripStatus(self):
        return self._tripStatus
    
    @tripStatus.setter
    def tripStatus(self,tripStatus):
        if type(tripStatus)!=int:
            Exception("tripStatus must be an integer between 1-5")
        if tripStatus<1 or tripStatus>5:
            Exception("tripStatus must be between 1 and 5")
        self._tripStatus=str(TripStatus(tripStatus))[11:]
    
    @property
    def paymentMode(self):
         return self._paymentMode

    @paymentMode.setter
    def paymentMode(self, paymentMode):
        if type(paymentMode)!=int:
            Exception("paymentMode must be an integer between 1-4")
        if paymentMode<1 or paymentMode>4:
            Exception("paymentMode must be between 1 and 4")
        self._paymentMode=str(PaymentMode(paymentMode))[12:]

 