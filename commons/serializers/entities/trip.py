from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField
from commons.serializers import commonserializer
from commons.datatypes.entities.trip import TripStatus, PaymentMode, ScheduleTripTransactionStatus, CompleteTripTransactionStatus
from commons.datatypes.entities.car import CarType
from commons import utils


class TripSerializer(commonserializer.CommonSerializer):
    tripId = serializers.IntegerField()
    carId = serializers.IntegerField()
    driverId = serializers.IntegerField()
    sourceLocation = PointField()
    destinationLocation = PointField()
    startTimeInEpochs = serializers.IntegerField()
    endTimeInEpochs = serializers.IntegerField()
    tripPrice = serializers.FloatField(min_value=0.0)
    tripStatus = serializers.ChoiceField(choices=utils.enumTuples(TripStatus))
    paymentMode = serializers.ChoiceField(choices=utils.enumTuples(PaymentMode))


class ScheduleTripTransactionInputSerializer(commonserializer.CommonSerializer):
    carType = serializers.ChoiceField(choices=utils.enumTuples(CarType))
    tripPrice = serializers.FloatField(min_value=0.0)
    sourceLocation = PointField()
    destinationLocation = PointField()


class ScheduleTripTransactionResultSerializer(commonserializer.CommonSerializer):
    scheduleTripTransactionStatus = serializers.ChoiceField(choices=utils.enumTuples(ScheduleTripTransactionStatus))
    trip = TripSerializer()


class CompleteTripTransactionInputSerializer(commonserializer.CommonSerializer):
    tripId = serializers.IntegerField()
    finishLocation = PointField()
    paymentMode = serializers.ChoiceField(choices=utils.enumTuples(PaymentMode))


class CompleteTripTransactionResultSerializer(commonserializer.CommonSerializer):
    completeTripTransactionStatus = serializers.ChoiceField(choices=utils.enumTuples(CompleteTripTransactionStatus))
    trip = TripSerializer()
