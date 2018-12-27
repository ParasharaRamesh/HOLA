from django.contrib.gis.geos import Point
from commons.datatypes.entities.location import GeoLocation
from commons import utils


class CarsInLocationRequest:
    def __init__(self, geoLocation):
        # FIXME: Check geoLocation
        # utils.objTypeCheck(geoLocation, Point, "geoLocation")
        self.geoLocation = geoLocation


class CarsInLocationResponse:
    def __init__(self, carStatuses):
        # FIXME: objTypeCheck for lists
        self.carStatuses = carStatuses
