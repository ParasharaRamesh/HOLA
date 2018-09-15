import json


class Car():
    carTypes=["UNKNOWN","CAR_TYPE_HATCHBACK","CAR_TYPE_SEDAN","CAR_TYPE_MINIVAN","CAR_TYPE_AUTO"]
    def __init__(self,carId=None,carType=None,carModel=None,carLicense=None):
        self.carId=carId#String
        if carType is None:
            raise Exception("carType is set as None")
        elif carType not in self.carTypes:
            raise Exception('carType ',carType,'is not supported as of now!')
        else:
            self.carType=carType#element in List(UNKNOWN,CAR_TYPE_HATCHBACK,CAR_TYPE_SEDAN,CAR_TYPE_MINIVAN)
        self.carModel=carModel#String
        self.carLicense=carLicense#String

    #serialzation function
    def toJSON(self):
        '''{"carId":"car_id_1","carType":"CAR_TYPE_HATCKBACK","carModel":"TOYATA","carLicense":"KA03 3122"}'''
        return {"carId":self.carId,"carType":self.carType,"carModel":self.carModel,"carLicense":self.carLicense}
 

    #Getters and Setters 
    def getCarId(self):
        return self.carId

    def setCarId(self,carId):
        self.carId=carId

    def getCarType(self):
        return self.getCarType
    
    def setCarType(self,carType):
        self.carType=carType
    
    def getCarModel(self):
        return self.carModel

    def setCarModel(self,carModel):
        self.carModel=carModel

    def getCarLicense(self):
        return self.carLicense

    def setCarLicense(self,carLicense):
        self.carLicense=carLicense    
    

 


