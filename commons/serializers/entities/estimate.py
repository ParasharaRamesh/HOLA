from rest_framework import serializers
from commons.serializers import commonserializer
from commons.datatypes.entities.car import CarType
from commons import utils


class EstimateForCarTypeSerializer(commonserializer.CommonSerializer):
    carType = serializers.ChoiceField(choices=utils.enumTuples(CarType))
    tripPrice = serializers.FloatField(min_value=0.0)
    discountAmount = serializers.FloatField(min_value=0.0)