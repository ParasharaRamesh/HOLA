from django.db import models
class Customer(models.Model):
    def __init__(self,customerId,name,email,phone,pastSevenDaysRideCount=0):
        self._customerId=customerId
        self._name=name
        self._email=email
        self._phone=phone
        self._pastSevenDaysRideCount=pastSevenDaysRideCount

    #getters and setters
    @property
    def customerId(self):
        return self._customerId

    @customerId.setter
    def customerId(self,customerId):
        self._customerId = customerId

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name=name

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,email):
        self._email=email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self,phone):
        self._phone = phone
    
    @property
    def pastSevenDaysRideCount(self):
        return self._pastSevenDaysRideCount

    @pastSevenDaysRideCount.setter
    def pastSevenDaysRideCount(self,pastSevenDaysRideCount):
        self._pastSevenDaysRideCount=pastSevenDaysRideCount
