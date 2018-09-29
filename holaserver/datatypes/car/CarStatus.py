import os
import enum
import sys
from copy import deepcopy
curr_path=os.path.dirname(__file__)
# print("currpath is ",curr_path)
lib_path = os.path.abspath(os.path.join(curr_path, '..','location'))
# print("lib path is ",lib_path)
sys.path.append(lib_path)
# from GeoLocation import GeoLocation
import GeoLocation


class CarAvailabilityStatus(enum.Enum):
    UNKNOWN=1
    CAR_OFF_DUTY=2
    CAR_AVAILABLE=3
    CAR_ON_TRIP=4
    CAR_ON_TRIP_CLOSE_TO_COMPLETION=5

class CarStatus:
    def __init__(self,carId,geoLocation,carAvailability):
        self._carId =carId
        if isinstance(geoLocation,GeoLocation.GeoLocation) == True:
            self._geoLocation=geoLocation
        else:
            Exception('The rvalue is of not of geolocation type!')

        if type(carAvailability)!=int:
            Exception("caravailability must be an integer between 1-5")
        if carAvailability<1 or carAvailability>5:
            Exception("caravailability must be between 1 and 5")
        self._carAvailability=str(CarAvailabilityStatus(carAvailability))[22:]

    def __str__(self):
        return '%s(%s)' % (type(self).__name__,', '.join('%s=%s' % item for item in vars(self).items()))

    #getters and setters
    @property
    def carId(self):
        return self._carId

    @carId.setter
    def carId(self,carId):
        self._carId=carId



    @property
    def carAvailability(self):
        return self._carAvailability

    @carAvailability.setter
    def carAvailability(self,carAvailability):
        if type(carAvailability)!=int:
            Exception("caravailability must be an integer between 1-5")
        if carAvailability<1 or carAvailability>5:
            Exception("caravailability must be between 1 and 5")
        self._carAvailability=str(CarAvailabilityStatus(carAvailability))[22:]

    @property
    def geoLocation(self):
        return self._geoLocation

    @geoLocation.setter
    def geoLocation(self,geoLocation):
        if isinstance(geoLocation,GeoLocation.GeoLocation) == True:
            self._geoLocation=geoLocation
        else:
            Exception('The rvalue is of not of geolocation type!')