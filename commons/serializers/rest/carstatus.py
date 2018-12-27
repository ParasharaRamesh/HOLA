from rest_framework import serializers
from commons.serializers import commonserializer
from commons.serializers.entities.car import CarStatusSerializer


class CarStatusRequestSerializer(commonserializer.CommonSerializer):
    carId = serializers.IntegerField()


class CarStatusResponseSerializer(commonserializer.CommonSerializer):
    carStatus = CarStatusSerializer()
