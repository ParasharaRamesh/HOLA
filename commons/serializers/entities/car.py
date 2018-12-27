from django.db import models
from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField
from commons.datatypes.entities.car import CarType, CarAvailability
from commons.serializers import commonserializer
from commons import utils


class CarSerializer(commonserializer.CommonSerializer):
    carId = serializers.IntegerField()
    carType = serializers.ChoiceField(choices=utils.enumTuples(CarType))
    carModel = serializers.CharField(max_length=64)
    carLicense = serializers.CharField(max_length=16)


class CarDriverSerializer(commonserializer.CommonSerializer):
    driverId = serializers.IntegerField()
    name = serializers.CharField(max_length=64)
    phone = serializers.CharField(max_length=10)
    rating = serializers.FloatField()
    feedbacks = serializers.ListField(child=serializers.CharField(max_length = 300))


class CarStatusSerializer(commonserializer.CommonSerializer):
    carId = serializers.IntegerField()
    geoLocation = PointField()
    carAvailability = serializers.ChoiceField(choices=utils.enumTuples(CarAvailability))
