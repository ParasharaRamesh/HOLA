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
    def __init__(self,geoLocation,carAvailability):
        if isinstance(geoLocation,GeoLocation.GeoLocation) == True:
            self._geoLocation=geoLocation
        else:
            Exception('The rvalue is of not of geolocation type!')

        if type(carAvailability)!=int:
            Exception("caravailability must be an integer between 1-5")
        if carAvailability<1 or carAvailability>5:
            Exception("caravailability must be between 1 and 5")
        self._carAvailability=str(CarAvailabilityStatus(carAvailability))[22:]

    #serialization function
    def __str__(self):
        '''{"geoLocation":{"latitude":12312.123,"longitude":12341234.2},"carAvailability":"CAR_AVAILABLE"}'''
    #    return "geoLocation:"+self.geoLocation+",carAvailability:"+self.carAvailability

    #getters and setters
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