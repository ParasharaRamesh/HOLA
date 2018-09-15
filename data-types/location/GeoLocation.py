class GeoLocation:
    def __init__(self,latitude,longitude):
        if type(latitude)==float and type(longitude)==float:
            self.latitude=latitude
            self.longitude=longitude
        else:
            raise Exception("Incorrect type for latitude and/or longitude!")

    #serialization function
    def toJSON(self):
        '''{"latitude":12312.123,"longitude":12341234.2}'''
        return {"latitude":self.latitude, "longitude":self.longitude}

    #getters and setters
    def getLatitude(self):
        return self.latitude
    
    def setLatitude(self,latitude):
        self.latitude = latitude
    
    def getLongitude(self):
        return self.longitude
    
    def setLongitude(self,longitude):
        self.longitude = longitude
    