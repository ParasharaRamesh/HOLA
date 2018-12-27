from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField
from commons.serializers import commonserializer
from commons.serializers.entities.car import CarStatusSerializer


class CarsInLocationRequestSerializer(commonserializer.CommonSerializer):
    geoLocation = PointField(required=True)


class CarsInLocationResponseSerializer(commonserializer.CommonSerializer):
    carStatuses = serializers.ListField(child=CarStatusSerializer())
