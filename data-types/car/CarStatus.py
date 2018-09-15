import os
import sys
curr_path=os.path.dirname(__file__)
# print("currpath is ",curr_path)
lib_path = os.path.abspath(os.path.join(curr_path, '..'))
# print("lib path is ",lib_path)
sys.path.append(lib_path)
from location.GeoLocation import GeoLocation


class CarStatus:
    carAvailabilityStatus=["UNKNOWN","CAR_OFF_DUTY","CAR_AVAILABLE","CAR_ON_TRIP","CAR_ON_TRIP_CLOSE_TO_COMPLETION"]
    def __init__(self,geoLocation=None,carAvailability=None):
        if geoLocation is None:
            raise Exception('geolocation attribute is None')
        elif not isinstance(geoLocation,GeoLocation):
            raise Exception("geolocation attribute is not of type \'GeoLocation\'")
        else:
            self.geoLocation=geoLocation
        if carAvailability is None:
            raise Exception("carAvailability is set as None")
        elif carAvailability not in self.carAvailabilityStatus:
            raise Exception("Not a valid Caravailabitiy status")
        else:
            self.carAvailability=carAvailability

    #serialization function
    def toJSON(self):
        '''{"geoLocation":{"latitude":12312.123,"longitude":12341234.2},"carAvailability":"CAR_AVAILABLE"}'''
        return {"geoLocation":self.geoLocation,"carAvailability":self.carAvailability}

    #getters and setters
    def getGeoLocation(self):
        return self.geoLocation

    def setGeoLocation(self,geoLocation):
        self.geoLocation=geoLocation

    def getCarAvailability(self):
        return self.carAvailability
    
    def setCarAvailability(self,carAvailability):
        if carAvailability is None:
            raise Exception("carAvailability is set as None")
        elif carAvailability not in self.carAvailabilityStatus:
            raise Exception("Not a valid Caravailabitiy status")
        else:
            self.carAvailability=carAvailability
