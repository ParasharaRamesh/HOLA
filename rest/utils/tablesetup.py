import csv
import os
import random
import time

from django.contrib.gis.geos import Point

from commons import utils
from commons.datatypes.entities.car import CarAvailability, CarType
from commons.datatypes.entities.trip import PaymentMode, TripStatus
from rest.models import CarStatusTable, CarDetailsTable, DriverDetailsTable, TripTable, RatingTable


# #added code for going around the GDAL Library improper configuration problem. Comment this if there are no issues....
# if os.name == 'nt':
#     import platform
#     OSGEO4W = r"C:\OSGeo4W"
#     if '64' in platform.architecture()[0]:
#         OSGEO4W += "64"
#     assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
#     os.environ['OSGEO4W_ROOT'] = OSGEO4W
#     os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal"
#     os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
#     os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']


class TableSetup:
    def __init__(self, numRows=1000, randomSeed=None):
        self.numRows = numRows
        random.seed(randomSeed)

    def initTables(self, tripTable=False):
        self.initCarDetailsTable()
        self.initDriverDetailsTable()
        self.initCarStatusTable()
        if tripTable:
            self.initTripAndRatingsTable()

    def clearAllTables(self):
        RatingTable.objects.all().delete()
        TripTable.objects.all().delete()
        CarStatusTable.objects.all().delete()
        DriverDetailsTable.objects.all().delete()
        CarDetailsTable.objects.all().delete()

    def initCarStatusTable(self):
        latBoundaries = [12.870595, 13.039963]
        lonBoundaries = [77.481075, 77.700260]
        self._positionCarsWithinBoundary(latBoundaries, lonBoundaries)

    def initCarDetailsTable(self):
        carModelsRows = self._read_csv("car-models.csv")
        rtoCodes = self._read_csv("bengaluru-rto-codes.csv")
        carTypeDict = dict(utils.enumTuples(CarType, valueFirst=False))

        carDetailsRowObjs = []
        for i in range(self.numRows):
            row = random.choice(carModelsRows)
            carLicense = random.choice(rtoCodes)[0] + " " + chr(i % 26 + 65) + " " + str(random.randrange(1000, 10000))
            carDetailsRowObj = CarDetailsTable(
                carId=i,
                carType=carTypeDict["CAR_TYPE_" + row[-1]],
                carModel=row[0] + " " + row[1],
                carLicense=carLicense
            )
            carDetailsRowObjs.append(carDetailsRowObj)
        CarDetailsTable.objects.bulk_create(carDetailsRowObjs)

    def initDriverDetailsTable(self):
        maleNames = self._read_csv("male-first-names.csv")
        femaleNames = self._read_csv("female-first-names.csv")
        pokemon = self._read_csv("pokemon.csv")
        randomFirstNames = random.choices(maleNames + femaleNames,
                                          weights=[95] * len(maleNames) + [5] * len(femaleNames),
                                          k=self.numRows)
        randomPokemon = random.choices(pokemon, k=self.numRows)

        driverDetailsRowObjs = []
        for i in range(self.numRows):
            driverDetailsRowObj = DriverDetailsTable(
                driverId=i,
                carId_id=i,
                name=randomFirstNames[i][0].capitalize() + " " + randomPokemon[i][0],
                phone=str(random.randrange(7 * 10 ** 9, 10 ** 10))
            )
            driverDetailsRowObjs.append(driverDetailsRowObj)
        DriverDetailsTable.objects.bulk_create(driverDetailsRowObjs)

    # def initRatingTable(self):
    #     latBoundaries = [12.870595, 13.039963]
    #     lonBoundaries = [77.481075, 77.700260]
    #     currentTime = time.time()
    #
    #     for i in range(self.numRows // 2, self.numRows):
    #         modNum = i % 4
    #         if modNum == 2
    #         if modNum == 2:
    #             startTimeInEpochs = currentTime - random.randrange(900, 3601)
    #             endTimeInEpochs = currentTime
    #         elif modNum == 3:
    #             startTimeInEpochs = currentTime - random.randrange(15, 901)
    #             endTimeInEpochs = currentTime
    #         else:
    #             startTimeInEpochs = currentTime - random.randrange(60, 901)
    #             endTimeInEpochs = None
    #         sourceLocation = self._createLocationWithinBoundary(latBoundaries, lonBoundaries)
    #         destinationLocation = self._createLocationWithinBoundary(latBoundaries, lonBoundaries)
    #         tripTableRowObj = TripTable(
    #             tripId=i,
    #             carId_id=i,
    #             driverId_id=i,
    #             customerId_id=2,
    #             sourceLocation=sourceLocation,
    #             destinationLocation=destinationLocation,
    #             startTimeInEpochs=startTimeInEpochs,
    #             endTimeInEpochs=endTimeInEpochs,
    #             tripPrice=random.randrange(39, 300),
    #             tripStatus=utils.enumTuples(TripStatus)[i % 4 + 1][0],
    #             paymentMode=utils.enumTuples(PaymentMode)[i % 3 + 1][0]
    #         )
    #         tripTableRowObjs.append(tripTableRowObj)
    #     TripTable.objects.bulk_create(tripTableRowObjs)

    def initTripAndRatingsTable(self):
        latBoundaries = [12.870595, 13.039963]
        lonBoundaries = [77.481075, 77.700260]
        currentTime = time.time()
        feedbacks = [
            "Perfect ride! Very fast!",
            "Nidaanavaagi chalisi",
            "Great conversation about Pokemon",
            "The driver never took the road not taken",
        ]
        tripTableRowObjs = []
        ratingTableRowObjs = []
        for i in range(self.numRows * 3):
            modNum = i % 4
            if modNum == 2:
                startTimeInEpochs = currentTime - random.randrange(900, 3601)
                endTimeInEpochs = currentTime
            elif modNum == 3:
                startTimeInEpochs = currentTime - random.randrange(15, 901)
                endTimeInEpochs = currentTime
            else:
                startTimeInEpochs = currentTime - random.randrange(60, 901)
                endTimeInEpochs = None
            sourceLocation = self._createLocationWithinBoundary(latBoundaries, lonBoundaries)
            destinationLocation = self._createLocationWithinBoundary(latBoundaries, lonBoundaries)
            tripTableRowObj = TripTable(
                tripId=i + 500,
                carId_id=i % self.numRows,
                driverId_id=i % self.numRows,
                customerId_id=2,
                sourceLocation=sourceLocation,
                destinationLocation=destinationLocation,
                startTimeInEpochs=startTimeInEpochs,
                endTimeInEpochs=endTimeInEpochs,
                tripPrice=random.randrange(39, 300),
                tripStatus=utils.enumTuples(TripStatus)[i % 4 + 1][0],
                paymentMode=utils.enumTuples(PaymentMode)[i % 3 + 1][0]
            )
            # if i % 4 + 1 == 4:
            ratingTableRowObj = RatingTable(
                tripId_id=i + 500,
                rating=random.randrange(3, 6),
                feedback=feedbacks[random.randrange(0, 4)]
            )
            ratingTableRowObjs.append(ratingTableRowObj)
            tripTableRowObjs.append(tripTableRowObj)
        TripTable.objects.bulk_create(tripTableRowObjs)
        RatingTable.objects.bulk_create(ratingTableRowObjs)

    def _positionCarsWithinBoundary(self, latBoundaries, lonBoundaries):
        for i in range(self.numRows):
            geoLocation = self._createLocationWithinBoundary(latBoundaries, lonBoundaries)
            carStatusRow = CarStatusTable(
                carId_id=i,
                carAvailability=utils.enumTuples(CarAvailability)[i % 3 + 1][0],
                geoLocation=geoLocation
            )
            carStatusRow.save()

    def _read_csv(self, filename, skipHeader=True):
        dataDir = os.path.join(os.path.abspath(os.path.dirname(__name__)), "rest", "data")
        with open(os.path.join(dataDir, filename)) as f:
            reader = csv.reader(f)
            if skipHeader:
                next(reader)
            return list(reader)

    def _createLocationWithinBoundary(self, latBoundaries, lonBoundaries):
        latitude = latBoundaries[0] + random.random() * (latBoundaries[1] - latBoundaries[0])
        longitude = lonBoundaries[0] + random.random() * (lonBoundaries[1] - lonBoundaries[0])
        return Point(x=longitude, y=latitude)
