from commons import utils
from commons.datatypes.entities.car import CarType

Rates = {
    CarType.CAR_TYPE_HATCHBACK.name: 10,
    CarType.CAR_TYPE_SEDAN.name: 13,
    CarType.CAR_TYPE_MINIVAN.name: 17,
}


class EstimateForCarType:
    def __init__(self, carType, tripPrice, discountAmount):
        utils.objTypeCheck(carType, CarType, "carType")

        self.carType = carType
        self.tripPrice = tripPrice
        self.discountAmount = discountAmount
