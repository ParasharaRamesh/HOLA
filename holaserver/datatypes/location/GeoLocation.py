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

    def __str__(self):
        return '%s(%s)' % (type(self).__name__,', '.join('%s=%s' % item for item in vars(self).items()))

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
        
    