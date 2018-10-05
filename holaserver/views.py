from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response#,status
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import datetime

from .models import *

from .datatypes.car import *
from .datatypes.trip import *

from .datatypes.car.Car import Car
from .datatypes.car.CarDriver import CarDriver
from .datatypes.trip.CompleteTripTransactionResult import CompleteTripTransactionResult
from .serializers.car.CarSerializer import CarSerializer
from .serializers.car.CarStatusSerializer import CarStatusSerializer
from .serializers.car.CarDriverSerializer import CarDriverSerializer
from .serializers.trip.CompleteTripTransactionResultSerializer import CompleteTripTransactionResultSerializer

from .datatypes.location import *
from .datatypes.estimate import *
from .datatypes.customer import *

from .serializers.customer import *
from .serializers.location import *
from .serializers.estimate import *
#from .serializers.trip import *

# Create your views here.

#FINISHED
class CarStatus(APIView):
    '''
    Pseudocode:
        .check input json ka all fields and check for NULL object passed and return appropriate error code.
        .use Carid to get caravailability and geolocation from CarStatusTable
    '''
    parser_classes = (JSONParser,)


    def post(self,request,format=None):
        if "carId" not in request.data or not isinstance(request.data["carId"], int):
            return Response({
            "result" : "failure",
            "message" : "Invalid data sent",
            })
        try:
            carStatusEntry = CarStatusTable.objects.get(carId=request.data["carId"])
        except CarStatusTable.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CarStatusSerializer(carStatusEntry)
        return Response(serializer.data)

#FINISHED
class CarDetails(APIView):
    '''   
    Pseudocode:
        .check input json ka all fields and check for NULL object passed and return appropriate error code.
        .use CarId and query the CarDetailsTable to get the carType,carModel,CarLicense for creating the CarDT in the response object
        .follow driverId and go to driverDetailsTable to get the name,phone&avg_ratings for creating the CarDriverDT
        .for getting the feedbacks go to the triptable and search for specific driverId and sort by triprating and get the top5 feedbacks and store it in a list and use that list to fill the CarDriverDT in the responseDT
        .Note:if driver has no feedbacks yet we return empty list.
    '''
    parser_classes = (JSONParser,)

    def post(self,request,format=None):
        if "carId" not in request.data or not isinstance(request.data["carId"], int):
            return Response({
            "result" : "failure",
            "message" : "Invalid data sent",
            })
        try:
            driverDetailsEntry = DriverDetailsTable.objects.get(carId=request.data["carId"])
        except DriverDetailsTable.DoesNotExist:
            return Response({
                "result" : "failure",
                "message" : "Driverdetails table doesnt have that object",
            })

        
        try:
            carDetailsEntry = CarDetailsTable.objects.get(carId=request.data["carId"])
        except CarDetailsTable.DoesNotExist:
            return Response({
                "result" : "failure",
                "message" : "Cardetails table doesnt have that object",
            })

        try:
            tripEntries = TripTable.objects.filter(carId=request.data["carId"]).order_by('-rating')[:5]
            feedbacks = [te.feedback for te in tripEntries]
            driverObject = CarDriver(driverDetailsEntry.driverId,driverDetailsEntry.name,driverDetailsEntry.phone,driverDetailsEntry.avg_rating,feedbacks)
            #driverObject.feedback=tripEntries#list of feedbacks
        except TripTable.DoesNotExist:
            return Response({
                "result" : "failure",
                "message" : "Trip table doesnt have that object",
            })

        carserializer = CarSerializer(carDetailsEntry)
        driverserializer = CarDriverSerializer(driverObject)
        return Response({"car":carserializer.data,"carDriver":driverserializer.data})

#FINISHED
class CancelTrip(APIView) :
    '''
       Pseudocode:
        .use the tripID and check the status 
        .if status ==TRIP_STATUS_SCHEDULED:
            .that means that this trip was scheduled before and we have to cancel it so set the status to TRIP_STATUS_CANCELLED 
            .set Car Status to CAR_AVAILABLE and then return the success/failure of this operation
            .either way take the user back to the getCarsInLocation screen.

    '''
    parser_classes = (JSONParser,)  

    def put(self, request, format=None):
        if "tripId" not in request.data or not isinstance(request.data["tripId"], int):
            return Response({
                "result" : "failure",
                "message" : "Invalid data sent",
            })
        
        try:
            tripEntry = TripTable.objects.get(tripId=request.data["tripId"])
        except TripTable.DoesNotExist:
            return Response({
                "result" : "failure",
                "message" : "Trip does not exist",
            })
        
        if tripEntry.tripStatus != "TRIP_STATUS_SCHEDULED":
            return Response({
                "result" : "failure",
                "message" : "Trip not scheduled",
            })
        
        tripEntry.tripStatus = "TRIP_STATUS_CANCELLED";
        tripEntry.save();
        # make car status available
        try:
            carEntry = CarStatusTable.objects.get(carId=tripEntry.carId.carId)
        except CarStatusTable.DoesNotExist:
            return Response({
                "result" : "failure",
                "message" : "Oops",
            })
        #should ideally set the carAvailbility as AVAILABLE for the next trip
        carEntry.carAvailability = "CAR_AVAILABLE"
        carEntry.save()

        return Response({"result" : "success"})


class CarsInLocation(APIView): 
    '''
    Pseudocode:
        .check input json ka all fields and check for NULL object passed and return appropriate error code.
        .use Carid to get caravailability and geolocation from CarStatusTable
    '''
    parser_classes = (JSONParser,)

class FareEstimate(APIView):
    #On entering source and destination , it should you the path on the map along with the fares for each car type
    #These classes get executed before the request comes to this API, ie these are policy attributes .. we might not need them now but for future use.
    parser_classes = (JSONParser,)

class ScheduleTrip(APIView):
    #On accepting a specific cartype this api is called which selects the nearest car and schedules it for you in the backend
    #These classes get executed before the request comes to this API, ie these are policy attributes .. we might not need them now but for future use.
    parser_classes = (JSONParser,)


#INCOMPLETE but started!!
class CompleteTrip(APIView):
    # Might be incorrect as of now have to test it out after finishing scheduleTrip API
    parser_classes = (JSONParser,)

    def put(self, request, format=None):
        if ("tripId" not in request.data or not isinstance(request.data["tripId"], int) or
                "finishLocation" not in request.data or
                "paymentMode" not in request.data or
                "rating" not in request.data or
                "feedback" not in request.data):
            return Response({
                "result" : "failure",
                "message" : "Invalid data sent",
            })

        try:
            tripEntry = TripTable.objects.get(tripId=request.data["tripId"])
        except TripTable.DoesNotExist:
            #tripObject = CompleteTripTransactionResult("TRIP_ID_NOT_FOUND",)
            return Response({
                "result" : "failure",
                "message" : "Trip doesn't exist",
            })
        
        tripEntry.endTimeInEpochs = "123" #datetime.datetime.utcnow()
        tripEntry.tripStatus = "TRIP_STATUS_COMPLETED"
        tripEntry.paymentMode = request.data["paymentMode"]
        #if tripEntry.destinationLocation != request.data["finishLocation"]
        #   tripEntry.destinationLocation = request.data["finishLocation"]
        tripEntry.save()

        #make car status available
        try:
            carEntry = CarStatusTable.objects.get(carId=tripEntry.carId.carId)
        except CarStatusTable.DoesNotExist:
            return Response({
                "result" : "failure",
                "message" : "Oops",
            })
        #should ideally verify if car was actually on trip
        carEntry.carAvailability = "CAR_AVAILABLE"
        carEntry.save()

        #update driver rating
        try:
            driverEntry = DriverDetailsTable.objects.get(carId=tripEntry.carId.carId)
        except DriverDetailsTable.DoesNotExist:
            return Response({
                "result" : "failure",
                "message" : "Oops",
            })
        driverEntry.avg_rating = (driverEntry.avg_rating + request.data["rating"]) / 2 # ???
        driverEntry.save()

        result = CompleteTripTransactionResult("SUCCESS", tripEntry)
        serializer = CompleteTripTransactionResultSerializer(result)
        
        return Response(serializer.data)