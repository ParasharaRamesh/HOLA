from rest_framework import serializers
from commons.serializers import commonserializer
from commons.serializers.entities.car import CarSerializer, CarDriverSerializer


class CarDetailsRequestSerializer(commonserializer.CommonSerializer):
    carId = serializers.IntegerField()


class CarDetailsReponseSerializer(commonserializer.CommonSerializer):
    car = CarSerializer()
    carDriver = CarDriverSerializer()
