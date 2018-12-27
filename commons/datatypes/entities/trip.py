from enum import Enum
from commons import utils
from commons.datatypes.entities.location import GeoLocation
from commons.datatypes.entities.car import CarType

# noinspection PyArgumentList
PaymentMode = Enum(
    value="PaymentMode",
    names=[
        "UNKNOWN",
        "CASH_PAYMENT",
        "CARD_PAYMENT",
        "PAYTM_PAYMENT",
    ])

# noinspection PyArgumentList
TripStatus = Enum(
    value="TripStatus",
    names=[
        "UNKNOWN",
        "TRIP_STATUS_SCHEDULED",
        "TRIP_STATUS_ONGOING",
        "TRIP_STATUS_COMPLETED",
        "TRIP_STATUS_CANCELLED",
        "TRIP_STATUS_COMPLETED_WITH_RATING",
    ])

# noinspection PyArgumentList
ScheduleTripTransactionStatus = Enum(
    value="ScheduleTripTransactionStatus",
    names=[
        "UNKNOWN",
        "SUCCESSFULLY_BOOKED",
        "PRICE_CHANGED",
        "NO_CARS_AVAILABLE",
        "DATABASE_ERROR",
    ])

# noinspection PyArgumentList
CompleteTripTransactionStatus = Enum(
    value="CompleteTripTransactionStatus",
    names=[
        "UNKNOWN",
        "SUCCESS",
        "PAYMENT_ERROR",
        "DATABASE_ERROR",
        "TRIP_ID_NOT_FOUND",
        "CANCELLED",
    ])

# noinspection PyArgumentList
CompleteTripOption = Enum(
    value="CompleteTripOption",
    names=[
        "DO_COMPLETE",
        "DO_CANCEL",
    ])


class Trip:
    def __init__(self, tripId, carId, driverId, sourceLocation, destinationLocation, startTimeInEpochs,
                 endTimeInEpochs, tripPrice, tripStatus, paymentMode):
        # utils.objTypeCheck(sourceLocation, GeoLocation, "sourceLocation")
        # utils.objTypeCheck(destinationLocation, GeoLocation, "destinationLocation")
        utils.objTypeCheck(tripStatus, TripStatus, "tripStatus")
        utils.objTypeCheck(paymentMode, PaymentMode, "paymentMode")

        self.tripId = tripId
        self.carId = carId
        self.driverId = driverId
        self.sourceLocation = sourceLocation
        self.destinationLocation = destinationLocation
        self.startTimeInEpochs = startTimeInEpochs
        self.endTimeInEpochs = endTimeInEpochs
        self.tripPrice = tripPrice
        self.tripStatus = tripStatus
        self.paymentMode = paymentMode


class ScheduleTripTransactionInput:
    def __init__(self, carType, tripPrice, sourceLocation, destinationLocation):
        utils.objTypeCheck(carType, CarType, "carType")
        # utils.objTypeCheck(sourceLocation, GeoLocation, "sourceLocation")
        # utils.objTypeCheck(destinationLocation, GeoLocation, "destinationLocation")

        self.carType = carType
        self.tripPrice = tripPrice
        self.sourceLocation = sourceLocation
        self.destinationLocation = destinationLocation


class ScheduleTripTransactionResult:
    def __init__(self, scheduleTripTransactionStatus, trip):
        utils.objTypeCheck(scheduleTripTransactionStatus, ScheduleTripTransactionStatus,
                           "scheduleTripTransactionStatus")
        utils.objTypeCheck(trip, Trip, "trip")

        self.scheduleTripTransactionStatus = scheduleTripTransactionStatus
        self.trip = trip


class CompleteTripTransactionInput:
    def __init__(self, tripId, finishLocation, paymentMode):
        utils.objTypeCheck(paymentMode, PaymentMode, "paymentMode")

        self.tripId = tripId
        self.finishLocation = finishLocation
        self.paymentMode = paymentMode


class CompleteTripTransactionResult:
    def __init__(self, completeTripTransactionStatus, trip):
        utils.objTypeCheck(
            completeTripTransactionStatus, CompleteTripTransactionStatus, "completeTripTransactionStatus")
        utils.objTypeCheck(trip, Trip, "trip")

        self.completeTripTransactionStatus = completeTripTransactionStatus
        self.trip = trip
