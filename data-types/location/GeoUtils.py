from GeoLocation import GeoLocation
from math import sin, cos, sqrt, atan2
class GeoUtils:
    def getDistanceBetweenLocationsInKms(self,sourceLoc,destinationLoc):
        if isinstance(sourceLoc,GeoLocation) and isinstance(destinationLoc,GeoLocation):
            return self.distance(sourceLoc.getLatitude(),sourceLoc.getLongitude(),destinationLoc.getLatitude(),destinationLoc.getLongitude(),0,0)
        else:
            raise Exception('sourceLoc and/or destLoc is not of type GeoLocation!')


    #some math function to compute the distance between 2 points, el1 and el2 are the altitude taken into consideration
    def distance(self,lat1,lon1,lat2,lon2,el1,el2):
        R = 6373.0
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = R * c
        height=el1 - el2
        distance = sqrt(height**2 + distance**2)
        return distance
