import os
import enum
import sys
curr_path=os.path.dirname(__file__)
# print("currpath is ",curr_path)
lib_path = os.path.abspath(os.path.join(curr_path, '..','location'))
print("in trip lib path is ",lib_path)
sys.path.append(lib_path)
import GeoLocation
lib_path = os.path.abspath(os.path.join(curr_path, '..','car'))
print("in trip lib path is ",lib_path)
sys.path.append(lib_path)
import Car

class ScheduleTripTransactionInput:
    def __init__(self,carType,tripPrice,sourceLocation,destinationLocation):
        if type(carType)!=int:
            Exception("cartype must be an integer between 1-5")
        if carType<1 or carType>5:
            Exception("cartype must be between 1 and 5")
        self._carType=str(Car.CarType(carType))[8:]#Enum

        if type(tripPrice)==float:
            self._tripPrice=tripPrice
        else:
            Exception("tripPrice rvalue must be a float type!")

        if isinstance(sourceLocation,GeoLocation.GeoLocation) == True:
            self._sourceLocation=sourceLocation
        else:
            Exception('The rvalue is of not of geolocation type!')

        if isinstance(destinationLocation,GeoLocation.GeoLocation) == True:
            self._destinationLocation=destinationLocation
        else:
            Exception('The rvalue is of not of geolocation type!')

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
        self._carType=str(Car.CarType(carType))[8:]#Enum

    @property
    def tripPrice(self):
        return self._tripPrice
    
    @tripPrice.setter
    def tripPrice(self,tripPrice):
        if type(tripPrice)==float:
            self._tripPrice=tripPrice
        else:
            Exception("tripPrice rvalue must be a float type!")


    @property
    def sourceLocation(self):
        return self._sourceLocation

    @sourceLocation.setter
    def sourceLocation(self,sourceLocation):
        if isinstance(sourceLocation,GeoLocation.GeoLocation) == True:
            self._sourceLocation=sourceLocation
        else:
            Exception('The rvalue is of not of geolocation type!')

    @property
    def destinationLocation(self):
        return self._destinationLocation

    @destinationLocation.setter
    def destinationLocation(self,destinationLocation):
        if isinstance(destinationLocation,GeoLocation.GeoLocation) == True:
            self._destinationLocation=destinationLocation
        else:
            Exception('The rvalue is of not of geolocation type!')
