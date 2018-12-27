from commons.datatypes.entities.car import CarType
from commons.datatypes.entities.location import GeoLocation
from commons.datatypes.entities.trip import ScheduleTripTransactionStatus, Trip
from commons import utils


class ScheduleTripRequest:
    def __init__(self, carType, tripPrice, sourceLocation, destinationLocation):
        utils.objTypeCheck(carType, CarType, "carType")
        # utils.objTypeCheck(sourceLocation, GeoLocation, "sourceLocation")
        # utils.objTypeCheck(destinationLocation, GeoLocation, "destinationLocation")

        self.carType = carType
        self.tripPrice = tripPrice
        self.sourceLocation = sourceLocation
        self.destinationLocation = destinationLocation


class ScheduleTripResponse:
    def __init__(self, scheduleTripStatus, trip):
        utils.objTypeCheck(scheduleTripStatus, ScheduleTripTransactionStatus, "scheduleTripStatus")
        utils.objTypeCheck(trip, Trip, "trip")

        self.scheduleTripStatus = scheduleTripStatus
        self.trip = trip
