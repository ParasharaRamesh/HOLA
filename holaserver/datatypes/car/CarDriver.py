TOP_COMMENTS = 5
class CarDriver:
    def __init__(self,driverId,name,phone,feedback):
        self._driverId=driverId#string
        self._name=name#string
        self._phone=phone#string
        #not sure if we should set rating everytime rather it should be trigger after every trip, or every new driver starts with a rating of 0.0
        self._rating=0.0
        self._feedbacks=[feedback]#List(string),his top5 best feedback , maybe feedback could be another class in itself not sure!


    #debug function 
    #support later
    def __str__(self):
        '''{"driverId":"driver_id_1","name":"MANJUNATH","phone":"9898712312","rating":4.3,"feedbacks":["great driver!,"I feel very safe with him driving"]}'''
        # return "driverId:"+self.driverId+",name:"+self.name+",phone:"+self.phone+",rating:"+self.rating+",feedbacks:"+self.feedbacks

    #Getters and Setters 
    @property
    def driverId(self):
        return self._driverId

    @driverId.setter
    def driverId(self,driverId):
        self._driverId=driverId

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name=name

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self,phone):
        self._phone=phone

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self,rating):
        if type(rating)==float:
            if rating >=0.0 and rating <=5.0:
                self._rating=rating
            else:
                Exception("rating is not inbetween 1.0 and 5.0!")
        else:
            Exception("rating rvalue is not of type float!")

    @property
    def feedbacks(self):
        return self._feedbacks

    @feedbacks.setter
    def feedbacks(self,feedback):
        if self._feedbacks == None:
            self._feedbacks=[feedback]
        elif len(self._feedbacks)<TOP_COMMENTS:
            self._feedbacks.append(feedback)
        #if there are 5 comments in this buffer already , then remove the first one and then insert another one in the end
        elif len(self._feedbacks) == TOP_COMMENTS:
            del self._feedbacks[0]#all feedbacks will anyway be there in the database! so we can always insert this later
            self._feedbacks.append(feedback)


