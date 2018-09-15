class CarDriver:
    def __init__(self,driverId=None,name=None,phone=None):
        self.driverId=driverId
        self.name=name
        self.phone=phone
        self.rating=0.0#based on triggers we need to populate this
        self.feedbacks=[]#his top5 best feedback , maybe feedback could be another class in itself not sure!

    #serialzation function
    def toJSON(self):
        '''{"driverId":"driver_id_1","name":"MANJUNATH","phone":"9898712312","rating":4.3,"feedbacks":["great driver!,"I feel very safe with him driving"]}'''
        return {"driverId":self.driverId,"name":self.name,"phone":self.phone,"rating":self.rating,"feedbacks":self.feedbacks}

    #getters and setters
    def getDriverId(self):
        return self.driverId

    def setDriverId(self,driverId):
        self.driverId=driverId

    def getName(self):
        return self.name

    def setName(self,name):
        self.name=name

    def getPhone(self):
        return self.phone

    def setPhone(self,phone):
        self.phone=phone

    def getRating(self):
        return self.rating

    def setRating(self,rating):
        self.rating=rating

    def getFeedbacks(self):
        return self.feedbacks

    def setFeedbacks(self,feedbacks):
        self.feedbacks=feedbacks

    def appendFeedbacks(self):
        pass

    def removeFeedbacks(self):
        pass

