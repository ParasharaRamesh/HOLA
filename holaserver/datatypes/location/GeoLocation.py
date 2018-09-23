class GeoLocation:
    def __init__(self,latitude,longitude):
        if type(latitude)==float:
            self._latitude=latitude
        else:
            raise Exception("Incorrect type for latitude must be float")

        if type(longitude)==float:
            self._longitude=longitude
        else:
            raise Exception("Incorrect type for longitude must be float")

    #debug function could be done later!
    def __str__(self):
        '''{"latitude":12312.123,"longitude":12341234.2}'''
        #return {"latitude":self.latitude, "longitude":self.longitude}

    #getters and setters
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self,latitude):
        if type(latitude)==float:
            self._latitude=latitude
        else:
            raise Exception("Incorrect type for latitude must be float")
        
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self,longitude):
        if type(longitude)==float:
            self._longitude=longitude
        else:
            raise Exception("Incorrect type for longitude must be float")
        
    