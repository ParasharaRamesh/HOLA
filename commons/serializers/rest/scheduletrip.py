from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField
from commons.serializers import commonserializer
from commons.serializers.entities.car import CarType
from commons.serializers.entities.trip import TripSerializer
from commons.datatypes.entities.trip import ScheduleTripTransactionStatus
from commons import utils


class ScheduleTripRequestSerializer(commonserializer.CommonSerializer):
    carType = serializers.ChoiceField(choices=utils.enumTuples(CarType))
    tripPrice = serializers.FloatField(min_value=0.0)
    sourceLocation = PointField()
    destinationLocation = PointField()


class ScheduleTripResponseSerializer(commonserializer.CommonSerializer):
        scheduleTripStatus = serializers.ChoiceField(choices=utils.enumTuples(ScheduleTripTransactionStatus))
        trip = TripSerializer()
