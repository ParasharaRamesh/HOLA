from GeoLocation import GeoLocation
from math import sin, cos, sqrt, atan2 ,degrees ,radians , acos , asin
class GeoUtils:
    def getDistanceBetweenLocationsInKms(self,sourceLoc,destinationLoc):
        if isinstance(sourceLoc,GeoLocation) and isinstance(destinationLoc,GeoLocation):
            return self.distance(sourceLoc.getLatitude(),sourceLoc.getLongitude(),destinationLoc.getLatitude(),destinationLoc.getLongitude(),0,0)
        else:
            raise Exception('sourceLoc and/or destLoc is not of type GeoLocation!')


    #some math function to compute the distance between 2 points, el1 and el2 are the altitude taken into consideration
    #get distance in kms
    def distance(self,lat1,lon1,lat2,lon2,el1=0,el2=0):
        R = 6373.0
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = R * c
        height=el1 - el2
        distance = sqrt(height**2 + distance**2)
        return distance

    def haversine(self,lat1,lon1,lat2,lon2):
        """
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians 
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles
        return c * r
    
    
