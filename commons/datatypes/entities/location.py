from math import sin, cos, sqrt, atan2, degrees, radians, acos, asin
from commons import utils


class GeoLocation:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude


class GeoUtils:
    AVG_EARTH_RADIUS = 6371  # Radius of Earth

    @staticmethod
    def getDistanceBetweenLocationsInKms(sourceLocation, destinationLocation):
        # utils.objTypeCheck(sourceLocation, GeoLocation, "sourceLocation")
        # utils.objTypeCheck(destinationLocation, GeoLocation, "destinationLocation")
        return GeoUtils.distance(sourceLocation["latitude"], sourceLocation["longitude"],
                                 destinationLocation["latitude"], destinationLocation["longitude"])

    @staticmethod
    def distance(lat1, lon1, lat2, lon2, alt1=0.0, alt2=0.0):
        latDistance = radians(lat2 - lat1)
        lonDistance = radians(lon2 - lon1)
        a = (sin(latDistance / 2) ** 2) + cos(radians(lat1)) * cos(radians(lat2)) * (sin(lonDistance / 2) ** 2)
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = GeoUtils.AVG_EARTH_RADIUS * c
        height = alt1 - alt2
        distance = sqrt(height ** 2 + distance ** 2)

        return distance

    @staticmethod
    def haversine(lat1, lon1, lat2, lon2):
        """
        Calculate the great-circle distance between two points on the Earth surface (in km).
        """
        # convert all latitudes/longitudes from decimal degrees to radians
        lat1, lon1, lat2, lon2 = map(radians, (lat1, lon1, lat2, lon2))

        # calculate haversine
        lat = lat2 - lat1
        lng = lon2 - lon1
        d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2
        h = 2 * GeoUtils.AVG_EARTH_RADIUS * asin(sqrt(d))

        return h
