from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField
from commons.serializers import commonserializer
from commons.serializers.entities.estimate import EstimateForCarTypeSerializer


class FareEstimatesRequestSerializer(commonserializer.CommonSerializer):
    sourceLocation = PointField()
    destinationLocation = PointField()


class FareEstimatesResponseSerializer(commonserializer.CommonSerializer):
    estimatesForCarTypes = serializers.ListField(child=EstimateForCarTypeSerializer())
