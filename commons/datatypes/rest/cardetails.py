from commons.datatypes.entities.car import Car, CarDriver
from commons import utils


class CarDetailsRequest:
    def __init__(self, carId):
        self.carId = carId


class CarDetailsResponse:
    def __init__(self, car, carDriver):
        utils.objTypeCheck(car, Car, "car")
        utils.objTypeCheck(carDriver, CarDriver, "carDriver")

        self.car = car
        self.carDriver = carDriver
