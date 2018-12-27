import time

from django.contrib.gis.geos import Point
from django.db import connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from commons.datatypes.entities.car import Car, CarDriver, CarStatus, CarAvailability, CarType
from commons.datatypes.entities.estimate import EstimateForCarType, Rates
from commons.datatypes.entities.location import GeoUtils
from commons.datatypes.entities.trip import TripStatus, Trip, CompleteTripOption, \
    CompleteTripTransactionStatus
from commons.datatypes.rest.cardetails import CarDetailsRequest, CarDetailsResponse
from commons.datatypes.rest.carsinlocation import CarsInLocationRequest, CarsInLocationResponse
from commons.datatypes.rest.carstatus import CarStatusRequest, CarStatusResponse
from commons.datatypes.rest.completetrip import CompleteTripRequest, CompleteTripResponse
from commons.datatypes.rest.fareestimates import FareEstimatesRequest, FareEstimatesResponse
from commons.datatypes.rest.ratetrip import RateTripRequest
from commons.datatypes.rest.scheduletrip import ScheduleTripRequest, ScheduleTripResponse
from commons.serializers.rest.cardetails import CarDetailsRequestSerializer, CarDetailsReponseSerializer
from commons.serializers.rest.carsinlocation import CarsInLocationRequestSerializer, CarsInLocationResponseSerializer
from commons.serializers.rest.carstatus import CarStatusRequestSerializer, CarStatusResponseSerializer
from commons.serializers.rest.completetrip import CompleteTripRequestSerializer, CompleteTripResponseSerializer
from commons.serializers.rest.fareestimates import FareEstimatesRequestSerializer, FareEstimatesResponseSerializer
from commons.serializers.rest.ratetrip import RateTripRequestSerializer
from commons.serializers.rest.scheduletrip import ScheduleTripRequestSerializer, ScheduleTripResponseSerializer
from .models import CarDetailsTable, DriverDetailsTable, CarStatusTable, TripTable, RatingTable


class FareEstimatesAPI(APIView):
    def post(self, request):
        serializer = FareEstimatesRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        fareEstimatesRequest = FareEstimatesRequest(**serializer.data)
        distance = GeoUtils.getDistanceBetweenLocationsInKms(
            fareEstimatesRequest.sourceLocation, fareEstimatesRequest.destinationLocation)

        estimatesForCarType = []
        for carType in CarType:
            if carType == CarType.UNKNOWN:
                continue
            # FIXME: Add sql query for streak
            estimatesForCarType.append(EstimateForCarType(carType.value, distance * Rates[carType.name], 0))

        fareEstimatesResponse = FareEstimatesResponse(estimatesForCarTypes=estimatesForCarType)
        return Response(FareEstimatesResponseSerializer(fareEstimatesResponse).data, status=status.HTTP_200_OK)


# FINISHED
class ScheduleTripAPI(APIView):
    def post(self, request):
        serializer = ScheduleTripRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        scheduleTripRequest = ScheduleTripRequest(**serializer.data)

        sourceLocation = scheduleTripRequest.sourceLocation
        destinationLocation = scheduleTripRequest.destinationLocation
        carType = scheduleTripRequest.carType

        carStatusRows = CarStatusTable.objects.nearbyOfType(latitude=sourceLocation["latitude"],
                                                            longitude=sourceLocation["longitude"],
                                                            carType=carType)

        if len(carStatusRows) == 0:
            return Response({"error": "no cars near location ."}, status=status.HTTP_404_NOT_FOUND)


        nearestCarStatusRow = carStatusRows[0]
        # update that car's availability as CAR_ON_TRIP
        nearestCarStatusRow.carAvailability = CarAvailability.CAR_ON_TRIP.value
        nearestCarStatusRow.save()

        # get the driverId associated with that car
        try:
            carDetailsRow = CarDetailsTable.objects.get(carId=nearestCarStatusRow.carId_id)
            driverDetailsRow = DriverDetailsTable.objects.get(carId=nearestCarStatusRow.carId_id)
        except (DriverDetailsTable.DoesNotExist, CarDetailsTable.DoesNotExist):
            return Response({"error": "Object does not exist."}, status=status.HTTP_404_NOT_FOUND)

        if not request.user.is_authenticated:
            return Response({"error": "User is not authenticated to take a trip"}, status=status.HTTP_400_BAD_REQUEST)

        source = Point(x=sourceLocation['longitude'], y=sourceLocation['latitude'])
        destination = Point(x=destinationLocation['longitude'], y=destinationLocation['latitude'])
        # create a tripTable entry
        currTime = int(time.time())
        newTripRow = TripTable(carId=carDetailsRow, driverId=driverDetailsRow, customerId=request.user,
                               sourceLocation=source, destinationLocation=destination, startTimeInEpochs=currTime,
                               endTimeInEpochs=0, tripPrice=scheduleTripRequest.tripPrice, tripStatus=2, paymentMode=1)
        newTripRow.save()
        trip = Trip(newTripRow.tripId, newTripRow.carId_id, newTripRow.driverId_id, newTripRow.sourceLocation,
                    newTripRow.destinationLocation, newTripRow.startTimeInEpochs,
                    newTripRow.endTimeInEpochs, newTripRow.tripPrice, newTripRow.tripStatus, newTripRow.paymentMode)
        scheduleTripResponse = ScheduleTripResponse(2, trip)
        return Response(ScheduleTripResponseSerializer(scheduleTripResponse).data, status=status.HTTP_200_OK)


# FINISHED
class CarDetailsAPI(APIView):
    def post(self, request):
        serializer = CarDetailsRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        carDetailsRequest = CarDetailsRequest(**serializer.data)

        try:
            carDetailsRow = CarDetailsTable.objects.get(carId=carDetailsRequest.carId)
            driverDetailsRow = DriverDetailsTable.objects.get(carId=carDetailsRequest.carId)
        except (DriverDetailsTable.DoesNotExist, CarDetailsTable.DoesNotExist):
            return Response({"error": "Object does not exist."}, status=status.HTTP_404_NOT_FOUND)

        car = Car(carDetailsRow.carId, carDetailsRow.carType, carDetailsRow.carModel, carDetailsRow.carLicense)
        carDriver = CarDriver(driverDetailsRow.driverId, driverDetailsRow.name, driverDetailsRow.phone)

        # TODO compute avg rating and the top 5 feedbacks about the driver
        # feedbacks =
        #     select rest_ratingtable.feedback as feedbacks
        #     from rest_ratingtable, rest_triptable
        #     where rest_ratingtable.tripId =  rest_triptable.tripId
        #     and rest_triptable.driverId = driverDetailsRow.driverId
        #     orderby rest_ratingtable.rating DESC limit 5

        with connection.cursor() as cursor:
            query = "SELECT AVG(t1.\"rating\") as avg_rating FROM rest_ratingtable as t1, rest_triptable as t2 " + \
                    "WHERE t1.\"tripId_id\" = t2.\"tripId\" AND t2.\"driverId_id\" = (%s) ;"
            params = (str(driverDetailsRow.driverId),)
            cursor.execute(query, params)
            average = cursor.fetchall()

        with connection.cursor() as cursor:
            query = "SELECT t1.\"feedback\" as feedbacks FROM rest_ratingtable as t1, rest_triptable as t2 " + \
                    "WHERE t1.\"tripId_id\" = t2.\"tripId\" AND t2.\"driverId_id\" = (%s) " + \
                    "ORDER BY t1.\"rating\" DESC LIMIT 3 ;"
            params = (str(driverDetailsRow.driverId),)
            cursor.execute(query, params)
            feedbacks = cursor.fetchall()

        # #compute the average of all the trips a particular driver has undergone
        carDriver.rating = average[0][0]
        # #store the feedbaccks in a list
        carDriver.feedbacks = [x[0] for x in feedbacks]

        carDetailsResponse = CarDetailsResponse(car=car, carDriver=carDriver)

        return Response(CarDetailsReponseSerializer(carDetailsResponse).data, status=status.HTTP_200_OK)


# FINISHED
class CarsInLocationAPI(APIView):
    def post(self, request):
        serializer = CarsInLocationRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        carsInLocationRequest = CarsInLocationRequest(**serializer.data)

        latitude = carsInLocationRequest.geoLocation["latitude"]
        longitude = carsInLocationRequest.geoLocation["longitude"]

        try:
            carStatusRows = CarStatusTable.objects.nearby(latitude, longitude)
        except CarStatusTable.DoesNotExist:
            return Response({"error": "Object does not exist."}, status=status.HTTP_404_NOT_FOUND)

        carStatuses = []
        for row in carStatusRows:
            carStatuses.append(
                CarStatus(carId=row.carId_id, geoLocation=row.geoLocation, carAvailability=row.carAvailability))

        carsInLocationResponse = CarsInLocationResponse(carStatuses=carStatuses)
        return Response(CarsInLocationResponseSerializer(carsInLocationResponse).data, status=status.HTTP_200_OK)


# FINISHED
class CarStatusAPI(APIView):
    def post(self, request):
        serializer = CarStatusRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        carStatusRequest = CarStatusRequest(**serializer.data)

        try:
            carStatusRow = CarStatusTable.objects.get(carId=carStatusRequest.carId)
        except CarStatusTable.DoesNotExist:
            return Response({"error": "Object does not exist."}, status=status.HTTP_404_NOT_FOUND)

        carStatus = CarStatus(carStatusRow.carId_id, carStatusRow.geoLocation, carStatusRow.carAvailability)
        carStatusResponse = CarStatusResponse(carStatus=carStatus)

        return Response(CarStatusResponseSerializer(carStatusResponse).data, status=status.HTTP_200_OK)


# FINISHED
class CompleteTripAPI(APIView):
    def post(self, request):
        serializer = CompleteTripRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        completeTripRequest = CompleteTripRequest(**serializer.data)

        try:
            tripRow = TripTable.objects.get(tripId=completeTripRequest.tripId)
        except TripTable.DoesNotExist:
            return Response({"error": "Object does not exist."}, status=status.HTTP_404_NOT_FOUND)

        tripRow.endTimeInEpochs = int(time.time())

        if tripRow.tripStatus == TripStatus.TRIP_STATUS_SCHEDULED.value:
            if completeTripRequest.completeTripOption == CompleteTripOption.DO_COMPLETE.value:
                tripRow.tripStatus = TripStatus.TRIP_STATUS_COMPLETED.value
            elif completeTripRequest.completeTripOption == CompleteTripOption.DO_CANCEL.value:
                tripRow.tripStatus = TripStatus.TRIP_STATUS_CANCELLED.value
        else:
            return Response({"error": "Can't complete trip not scheduled."}, status=status.HTTP_400_BAD_REQUEST)

        tripRow.paymentMode = completeTripRequest.paymentMode
        tripRow.destinationLocation = Point(x=completeTripRequest.finishLocation["longitude"],
                                            y=completeTripRequest.finishLocation["latitude"])
        tripRow.save()

        # make car status available
        try:
            carRow = CarStatusTable.objects.get(carId=tripRow.carId_id)
        except CarStatusTable.DoesNotExist:
            return Response({"error": "Object does not exist."}, status=status.HTTP_404_NOT_FOUND)
        # should ideally verify if car was actually on trip
        carRow.carAvailability = CarAvailability.CAR_AVAILABLE.value
        carRow.geoLocation = Point(x=completeTripRequest.finishLocation["longitude"],
                                   y=completeTripRequest.finishLocation["latitude"])
        carRow.save()

        try:
            driverEntry = DriverDetailsTable.objects.get(carId=tripRow.carId_id)
        except DriverDetailsTable.DoesNotExist:
            return Response({"error": "Object does not exist."}, status=status.HTTP_404_NOT_FOUND)

        trip = Trip(tripRow.tripId, tripRow.carId_id, driverEntry.driverId,
                    tripRow.sourceLocation, tripRow.destinationLocation, tripRow.startTimeInEpochs,
                    tripRow.endTimeInEpochs, tripRow.tripPrice, tripRow.tripStatus, tripRow.paymentMode)

        if tripRow.tripStatus == TripStatus.TRIP_STATUS_COMPLETED.value:
            completeTripStatus = CompleteTripTransactionStatus.SUCCESS.value
        else:
            completeTripStatus = CompleteTripTransactionStatus.CANCELLED.value

        completeTripResponse = CompleteTripResponse(completeTripStatus, trip)
        return Response(CompleteTripResponseSerializer(completeTripResponse).data, status=status.HTTP_200_OK)


# FINISHED
class RateTripAPI(APIView):
    def post(self, request):
        serializer = RateTripRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        rateTripRequest = RateTripRequest(**serializer.data)

        try:
            tripRow = TripTable.objects.get(tripId=rateTripRequest.tripId)
        except TripTable.DoesNotExist:
            return Response({"error": "Object does not exist."}, status=status.HTTP_404_NOT_FOUND)

        # rate a trip only if it has been completed:
        if tripRow.tripStatus == TripStatus.TRIP_STATUS_COMPLETED.value:
            ratingRow = RatingTable(tripId_id=rateTripRequest.tripId, rating=rateTripRequest.rating,
                                    feedback=rateTripRequest.feedback)
            ratingRow.save()
            tripRow.tripStatus = TripStatus.TRIP_STATUS_COMPLETED_WITH_RATING.value
            tripRow.save()
            return Response({"success": "feedback and rating saved.."}, status=status.HTTP_200_OK)
        elif tripRow.tripStatus == TripStatus.TRIP_STATUS_COMPLETED_WITH_RATING.value:
            return Response({"error": "Trip has already been given a rating !!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Trip must be completed in order to give a rating."},
                            status=status.HTTP_400_BAD_REQUEST)
