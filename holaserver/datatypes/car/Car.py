import json
import enum


class CarType(enum.Enum):
    UNKNOWN=1
    CAR_TYPE_HATCHBACK=2
    CAR_TYPE_SEDAN=3
    CAR_TYPE_MINIVAN=4
    CAR_TYPE_AUTO=5

class Car():
    def __init__(self,carId,carType,carModel,carLicense):
        self._carId=carId#String
        if type(carType)!=int:
            Exception("cartype must be an integer between 1-5")
        if carType<1 or carType>5:
            Exception("cartype must be between 1 and 5")
        self._carType=str(CarType(carType))[8:]#Enum

        self._carModel=carModel#String
        self._carLicense=carLicense#String

    def __str__(self):
        return '%s(%s)' % (type(self).__name__,', '.join('%s=%s' % item for item in vars(self).items()))
 

    #Getters and Setters 
    @property
    def carId(self):
        return self._carId

    @carId.setter
    def carId(self,carId):
        self._carId=carId

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
    def carModel(self):
        return self._carModel

    @carModel.setter
    def carModel(self,carModel):
        self._carModel=carModel


    @property
    def carLicense(self):
        return self._carLicense

    @carLicense.setter
    def carLicense(self,carLicense):
        self._carLicense=carLicense    
    
if __name__=="__main__":
    car=Car()
    car.carType=1
    print(car.carType)
    print(type(car.carType))

 


