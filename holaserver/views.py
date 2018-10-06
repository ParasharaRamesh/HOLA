from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response#,status
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import datetime
import time

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
from .serializers.location.GeoLocationSerializer import GeoLocationSerializer

from .datatypes.location.GeoLocation import GeoLocation
from .datatypes.location.GeoUtils import *

from .datatypes.estimate import *
from .datatypes.customer import *

from .serializers.customer import *

from .serializers.estimate import *

from .GlobalConstants import *
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

#FINISHED
class CarsInLocation(APIView): 
    '''
        Pseudocode:
        .check input json ka all fields and check for NULL object passed and return appropriate error code.
        .Return list of cars that are CarStatus.CarAvailability.CAR_AVAILABLE &
                       within GlobalConstants.SEARCH_RADIUS(inclusive) from CarStatusTable.
        .Use GlobalConstants.HAVER_SINE_FORMULA to calculate the distance between two lat/longs.
        .Note:there is no GlobalConstants file as of now , but if you want to create it you can refer datatypes.loction.GeoUtils for HAVER_SINE_FORMULA,also have a threshold for FareEstimate discount

        .check input json ka all fields and check for NULL object passed and return appropriate error code.
        .use Carid to get caravailability and geolocation from CarStatusTable
    '''
    #carId,geolocation,caravailability ==>carstatusDT
    parser_classes = (JSONParser,)
    def post(self,request,format=None):
        if "geoLocation" not in request.data:
            print("request is ",type(request.data))
            return Response({
            "result" : "failure",
            "message" : "input JSON does not have geoLocation",
            })
        #checking if geoLocation is of valid geolocation datatype    
        else:
            inputJSONcontent = JSONRenderer().render(request.data["geoLocation"])
            stream=BytesIO(inputJSONcontent)
            inputJSON=JSONParser().parse(stream)
            serializer = GeoLocationSerializer(data=inputJSON)
            if not serializer.is_valid():
                return Response({
                "result" : "failure",
                "message" : "input JSON is not of geoLocation type",
                })

        inputLat = request.data["geoLocation"]["latitude"]
        inputLong = request.data["geoLocation"]["longitude"]

        try:
            carStatusEntries = CarStatusTable.objects.filter(carAvailability="CAR_AVAILABLE")
            carStatusEntriesNearLocation = list(filter(lambda t: isNearLocation(inputLat,inputLong,t.geoLocation.latitude,t.geoLocation.longitude), carStatusEntries))
        except CarStatusTable.DoesNotExist:
            return Response({
                "result" : "failure",
                "message" : "No cars found near given location",
            })
        serializerList =[CarStatusSerializer(carStatus) for carStatus in carStatusEntriesNearLocation]
        return Response({"carStatuses":[serializer.data for serializer in serializerList]})

#To be done
class FareEstimate(APIView):
    '''
    Pseudocode:
        .check input json ka all fields and check for NULL object passed and return appropriate error code.
        .use datatypes.loction.GeoUtils.getDistanceBetweenLocationInKms to get the distance between source and destination Location.
        .create a List<estimatesForCarType DT> for each type of car:ie hatch_back,sedan etc
        .use the customerId to go to CustomerDetails table and get the streakfor past7 days let it be k.(Use the Trip table to directly write a query to get the count )  
        .if k > GlobalConstants.threshold(not yet created!) then assign a discount of say x%
        .for each estimatesForCarTypeDT assign the tripPrice as the distance*perkmcost for that carType
        .for each estimatesForCarTypeDT assign the discountedTripPrice as tripPrice(1-(x/100))
        .return this list of estimatesForCarTypes
        .Note : for the perkmcost of each cartype have a dictionary<cartype,perkmcost> in global constants !(to be created)
    '''
    parser_classes = (JSONParser,)

#to be done
class ScheduleTrip(APIView):
    '''
    PsuedoCode"
        .check input json ka all fields and check for NULL object passed and return appropriate error code.
        .use datatypes.loction.GeoUtils.getDistanceBetweenLocationInKms to get the distance between source and destination Location.
        .create a List<estimatesForCarType DT> for each type of car:ie hatch_back,sedan etc
        .use the customerId to go to CustomerDetails table and get the streakfor past7 days let it be k.(Use the Trip table to directly write a query to get the count   
        .if k > GlobalConstants.threshold(not yet created!) then assign a discount of say x%
        .for each estimatesForCarTypeDT assign the tripPrice as the distance*perkmcost for that carType
        .for each estimatesForCarTypeDT assign the discountedTripPrice as tripPrice(1-(x/100))
        .return this list of estimatesForCarTypes
        .Note : for the perkmcost of each cartype have a dictionary<cartype,perkmcost> in global constants !(to be created)
    '''
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
                "completeTripTransactionStatus" : "TRIP_ID_NOT_FOUND",
                "result" : "failure",
                "message" : "Invalid data sent",
            })
        #checking if geoLocation is of valid geolocation datatype    
        else:
            inputJSONcontent = JSONRenderer().render(request.data["finishLocation"])
            stream=BytesIO(inputJSONcontent)
            inputJSON=JSONParser().parse(stream)
            serializer = GeoLocationSerializer(data=inputJSON)
            if not serializer.is_valid():
                return Response({
                "result" : "failure",
                "message" : "input JSON is not of geoLocation type",
                })
        try:
            tripEntry = TripTable.objects.get(tripId=request.data["tripId"])
        except TripTable.DoesNotExist:
            #tripObject = CompleteTripTransactionResult("TRIP_ID_NOT_FOUND",)
            # check this
            return Response({
                "completeTripTransactionStatus" : "TRIP_ID_NOT_FOUND",
                "message" : "Trip doesn't exist",
            })
        
        tripEntry.endTimeInEpochs = int(time.mktime(datetime.datetime.now().timetuple()))
        tripEntry.tripStatus = "TRIP_STATUS_COMPLETED"
        tripEntry.paymentMode = request.data["paymentMode"]
        if (tripEntry.destinationLocation.latitude != request.data["finishLocation"]["latitude"] or
                tripEntry.destinationLocation.longitude != request.data["finishLocation"]["longitude"]):
            tripEntry.destinationLocation.latitude = request.data["finishLocation"]["latitude"]
            tripEntry.destinationLocation.longitude = request.data["finishLocation"]["longitude"]
        tripEntry.rating = request.data["rating"]
        tripEntry.feedback = request.data["feedback"]
        tripEntry.save()

        #make car status available
        try:
            carEntry = CarStatusTable.objects.get(carId=tripEntry.carId.carId)
        except CarStatusTable.DoesNotExist:
            return Response({
                "completeTripTransactionStatus" : "DATABASE_ERROR",
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
                "completeTripTransactionStatus" : "DATABASE_ERROR",
                "result" : "failure",
                "message" : "Oops",
            })
        driverEntry.avg_rating = (driverEntry.avg_rating + request.data["rating"]) / 2 # ???
        driverEntry.save()

        tripObject = Trip(tripEntry.tripId, tripEntry.carId.carId, driverEntry.driverId, tripEntry.customerId.customerId, tripEntry.sourceLocation,
                        tripEntry.destinationLocation, tripEntry.startTimeInEpochs, tripEntry.endTimeInEpochs,
                        tripEntry.tripPrice, 4, tripEntry.paymentMode, tripEntry.rating, tripEntry.feedback)

        result = CompleteTripTransactionResult(2, tripObject)
        serializer = CompleteTripTransactionResultSerializer(result)
        
        return Response(serializer.data)