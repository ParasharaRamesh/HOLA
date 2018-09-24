import sys
import os
curr_path=os.path.dirname(__file__)
# print("currpath is ",curr_path)
lib_path = os.path.abspath(os.path.join(curr_path, '..','car'))
# print("lib path is ",lib_path)
sys.path.append(lib_path)
from Car import CarType

class EstimateForCarType:
    def __init__(self,carType,tripPrice,discountTripPrice):
        self._carType=str(CarType(carType))[8:]#None#car.Cartype,enum
        self._tripPrice=tripPrice#None#float
        self._discountTripPrice=discountTripPrice
    
    def __str__(self):
        '''{"carType":"CAR_TYPE_HATCHBACK","tripPrice": 129.00}'''
        # return {"carType":self.carType,"tripPrice":self.tripPrice}
    
    #getters and setters
    @property
    def carType(self):
        return self._carType

    @carType.setter
    def carType(self,carType):
        if type(carType)!=int:
            Exception("cartype must be an integer between 1-5")
        if carType<1 or carType>5:
            Exception("cartype must be between 1 and 5")
        self._carType=str(CarType(carType))[8:]
    
    @property
    def tripPrice(self):
        return self._tripPrice

    @tripPrice.setter
    def tripPrice(self,tripPrice):
        if type(tripPrice)==float:
            self._tripPrice = tripPrice
        else:
            Exception("trip Price rvalue must be of type float")

    @property
    def discountTripPrice(self):
        return self._discountTripPrice

    @discountTripPrice.setter
    def discountTripPrice(self,discountTripPrice):
        if type(discountTripPrice)==float:
            self._discountTripPrice= discountTripPrice
        else:
            Exception("discountTripPrice rvalue must be of type float")
