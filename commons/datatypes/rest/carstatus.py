from commons.datatypes.entities.car import CarStatus
from commons import utils


class CarStatusRequest:
    def __init__(self, carId):
        self.carId = carId


class CarStatusResponse:
    def __init__(self, carStatus):
        utils.objTypeCheck(carStatus, CarStatus, "carStatus")
        self.carStatus = carStatus
