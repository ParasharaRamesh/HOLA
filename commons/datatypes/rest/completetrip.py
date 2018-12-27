from commons.datatypes.entities.location import GeoLocation
from commons.datatypes.entities.trip import PaymentMode, CompleteTripTransactionStatus, CompleteTripOption, Trip
from commons import utils


class CompleteTripRequest:
    def __init__(self, tripId, completeTripOption, finishLocation, paymentMode):
        # utils.objTypeCheck(finishLocation, GeoLocation, "finishLocation")
        utils.objTypeCheck(paymentMode, PaymentMode, "paymentMode")
        utils.objTypeCheck(completeTripOption, CompleteTripOption, "completeTripOption")

        self.tripId = tripId
        self.completeTripOption = completeTripOption
        self.finishLocation = finishLocation
        self.paymentMode = paymentMode


class CompleteTripResponse:
    def __init__(self, completeTripStatus, trip):
        utils.objTypeCheck(completeTripStatus, CompleteTripTransactionStatus, "completeTripStatus")
        utils.objTypeCheck(trip, Trip, "trip")

        self.completeTripStatus = completeTripStatus
        self.trip = trip
