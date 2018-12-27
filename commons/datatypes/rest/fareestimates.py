from commons.datatypes.entities.location import GeoLocation
from commons import utils


class FareEstimatesRequest:
    def __init__(self, sourceLocation, destinationLocation):
        # utils.objTypeCheck(sourceLocation, GeoLocation, "sourceLocation")
        # utils.objTypeCheck(destinationLocation, GeoLocation, "destinationLocation")

        self.sourceLocation = sourceLocation
        self.destinationLocation = destinationLocation


class FareEstimatesResponse:
    def __init__(self, estimatesForCarTypes):
        # FIXME: objTypeCheck for list
        self.estimatesForCarTypes = estimatesForCarTypes
