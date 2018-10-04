from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response#,status
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .models import *
from .serializers.car.CarStatusSerializer import CarStatusSerializer

# Create your views here.
class CarsInLocation(APIView): 
    #On entering the app, show all the cars around your current location
    #These classes get executed before the request comes to this API, ie these are policy attributes .. we might not need them now but for future use.
    parser_classes = (JSONParser,)

class FareEstimate(APIView):
    #On entering source and destination , it should you the path on the map along with the fares for each car type
    #These classes get executed before the request comes to this API, ie these are policy attributes .. we might not need them now but for future use.
    parser_classes = (JSONParser,)

class ScheduleTrip(APIView):
    #On accepting a specific cartype this api is called which selects the nearest car and schedules it for you in the backend
    #These classes get executed before the request comes to this API, ie these are policy attributes .. we might not need them now but for future use.
    parser_classes = (JSONParser,)

class CarStatus(APIView):
    '''
    Pseudocode:
        .check input json ka all fields and check for NULL object passed and return appropriate error code.(Taken care of internally!)
        .use CarId and query the CarDetailsTable to get the carType,carModel,CarLicense for creating the CarDT in the response object
        .follow driverId and go to driverDetailsTable to get the name,phone&avg_ratings for creating the CarDriverDT
        .for getting the feedbacks go to the triptable and search for specific driverId and sort by triprating and get the top5 feedbacks and store it in a list and use that list to fill the CarDriverDT in the responseDT
        .Note:if driver has no feedbacks yet we return empty list.
    '''
    parser_classes = (JSONParser,)


    def get(self,request,format=None):
        inpCarId = request.data['carId']
        try:
            carStatusEntry = CarStatusTable.objects.get(id=inpCarId)
        except CarStatusTable.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        print("entries are",carStatusEntry)
        serializer = CarStatusSerializer(carStatusEntry,many=True)
        return Response(serializer.data)

# use the below code to test the rest api!
# from rest_framework.test import APIRequestFactory

# # Using the standard RequestFactory API to create a form POST request
# factory = APIRequestFactory()
# request = factory.post('/notes/', {'title': 'new idea'})
     

class CarDetails(APIView):
    # On scheduling a trip it takes the user to a screen where he can see the driver details along with a "confirm" or "cancel" button.This API is mainly used to show the driver details
    #These classes get executed before the request comes to this API, ie these are policy attributes .. we might not need them now but for future use.
    parser_classes = (JSONParser,)

    def get(self,request,format=None):
        pass



class CancelTrip(APIView) :
    # If the user presses "cancel" then it takes the user back to the home screen which is the map view with all the "CarsInLocation".Internally it just makes the cancelled car available for scheduling the next time
    #These classes get executed before the request comes to this API, ie these are policy attributes .. we might not need them now but for future use.
    parser_classes = (JSONParser,)  

    def put(self, request, format=None):
        if "tripId" not in request.data or not isinstance(request.data["tripId"], int):
            return Response({
                "result" : "failure",
                "message" : "Invalid data sent",
            })
        
        try:
            tripEntry = TripTable.objects.get(id=request.data["tripId"])
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
            carEntry = CarStatusTable.objects.get(carId=tripEntry.carId.id)
        except CarStatusTable.DoesNotExist:
            return Response({
                "result" : "failure",
                "message" : "Oops",
            })
        #should ideally verify if car was actually on trip
        carEntry.carAvailability = "CAR_AVAILABLE"
        carEntry.save()

        return Response({"result" : "success"})

class CompleteTrip(APIView):
    # If the user presses "confirm" then it internally finshes a trip which transports the car to the destination location and it stays there until the next time somone books a cab.The user is then prompted to enter feedback and give a rating of the driver for that particular trip
    #These classes get executed before the request comes to this API, ie these are policy attributes .. we might not need them now but for future use.
    parser_classes = (JSONParser,)
