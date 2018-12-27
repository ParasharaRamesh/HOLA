from django.contrib.gis.db import models
from django.db import connection
from django.contrib.auth.models import User
from commons import utils, constants
from commons.datatypes.entities.car import CarType, CarAvailability
from commons.datatypes.entities.trip import TripStatus, PaymentMode


class CarStatusManager(models.Manager):
    def nearby(self, latitude, longitude):
        with connection.cursor() as cursor:
            hsf = constants.HAVER_SINE_FORMULA.format(latitude=latitude, longitude=longitude)
            query = "SELECT * " + \
                    "FROM rest_carstatustable as cst " + \
                    "WHERE (" + hsf + ")" + "<=" + str(constants.SEARCH_RADIUS) + " " \
                    "AND \"carAvailability\"=" + str(CarAvailability.CAR_AVAILABLE.value) + " " \
                    "ORDER BY (" + hsf + ") ASC;"
            cursor.execute(query)

            result_list = []
            print("nearby:")
            for row in cursor.fetchall():
                print(row[3])
                carStatusRow = self.model(id=row[0], carAvailability=row[1], geoLocation=row[2], carId_id=row[3])
                result_list.append(carStatusRow)
        return result_list

    def nearbyOfType(self, latitude, longitude, carType):
        with connection.cursor() as cursor:
            hsf = constants.HAVER_SINE_FORMULA.format(latitude=latitude, longitude=longitude)
            query = "SELECT (t1).* " + \
                    "FROM rest_carstatustable as t1, rest_cardetailstable as t2 " + \
                    "WHERE (" + hsf + ")" + "<=" + str(constants.SEARCH_RADIUS) + " " + \
                    "AND t1.\"carId_id\"=t2.\"carId\" " + \
                    "AND t1.\"carAvailability\"=" + str(CarAvailability.CAR_AVAILABLE.value) + " " + \
                    "AND t2.\"carType\"=" + str(carType) + " " + \
                    "ORDER BY " + hsf + " ASC " + \
                    "LIMIT 5;"
            cursor.execute(query)

            result_list = []
            print("nearybyOfType")
            for row in cursor.fetchall():
                print(row[3])
                carStatusRow = self.model(id=row[0], carAvailability=row[1], geoLocation=row[2], carId_id=row[3])
                result_list.append(carStatusRow)
        return result_list


class CarDetailsTable(models.Model):
    carId = models.AutoField(primary_key=True)
    carType = models.IntegerField(choices=utils.enumTuples(CarType), default=CarType.UNKNOWN.value)
    carModel = models.CharField(max_length=64)
    carLicense = models.CharField(max_length=16)

    class Meta:
        verbose_name_plural = "CarDetailsTable"


class CarStatusTable(models.Model):
    carId = models.ForeignKey(CarDetailsTable, verbose_name="carId", on_delete=models.DO_NOTHING)
    carAvailability = models.IntegerField(choices=utils.enumTuples(CarAvailability),
                                          default=CarAvailability.UNKNOWN.value)
    geoLocation = models.PointField()
    objects = CarStatusManager()

    class Meta:
        verbose_name_plural = "CarStatusTable"


class DriverDetailsTable(models.Model):
    driverId = models.AutoField(primary_key=True)
    carId = models.OneToOneField(CarDetailsTable, verbose_name="carId", on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "DriverDetailsTable"


class TripTable(models.Model):
    tripId = models.AutoField(primary_key=True)
    carId = models.ForeignKey(CarDetailsTable, verbose_name="carId", on_delete=models.DO_NOTHING)
    driverId = models.ForeignKey(DriverDetailsTable, verbose_name="driverId", on_delete=models.DO_NOTHING)
    customerId = models.ForeignKey(User, verbose_name="customerId", on_delete=models.DO_NOTHING, default = None)#see how to fit this
    sourceLocation = models.PointField()
    destinationLocation = models.PointField()
    startTimeInEpochs = models.PositiveIntegerField()
    endTimeInEpochs = models.PositiveIntegerField(null=True)
    tripPrice = models.FloatField()
    tripStatus = models.IntegerField(choices=utils.enumTuples(TripStatus), default=TripStatus.UNKNOWN.value)
    paymentMode = models.IntegerField(choices=utils.enumTuples(PaymentMode), default=PaymentMode.UNKNOWN.value)

    class Meta:
        verbose_name_plural = "TripTable"


class RatingTable(models.Model):
    tripId = models.ForeignKey(TripTable, verbose_name="tripId", on_delete=models.DO_NOTHING)
    rating = models.FloatField()
    feedback = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "RatingTable"
