from enum import Enum
from django.contrib.gis.geos import Point
from commons import utils

# noinspection PyArgumentList
CarType = Enum(
    value="CarType",
    names=[
        "UNKNOWN",
        "CAR_TYPE_HATCHBACK",
        "CAR_TYPE_SEDAN",
        "CAR_TYPE_MINIVAN",
    ])

# noinspection PyArgumentList
CarAvailability = Enum(
    value="CarAvailability",
    names=[
        "UNKNOWN",
        "CAR_OFF_DUTY",
        "CAR_AVAILABLE",
        "CAR_ON_TRIP",
        "CAR_ON_TRIP_CLOSE_TO_COMPLETION"
    ])


class Car:
    def __init__(self, carId, carType, carModel, carLicense):
        utils.objTypeCheck(carType, CarType, "carType")

        self.carId = carId
        self.carType = carType
        self.carModel = carModel
        self.carLicense = carLicense


class CarDriver:
    def __init__(self, driverId, name, phone):
        self.driverId = driverId
        self.name = name
        self.phone = phone
        #assigned only in cardetailsAPI call
        self.rating = None
        self.feedbacks = None


class CarStatus:
    def __init__(self, carId, geoLocation, carAvailability):
        utils.objTypeCheck(geoLocation, Point, "geoLocation")
        utils.objTypeCheck(carAvailability, CarAvailability, "carAvailability")

        self.carId = carId
        self.geoLocation = geoLocation
        self.carAvailability = carAvailability
