from rest_framework import serializers
from commons.serializers import commonserializer
from commons.serializers.entities.trip import TripSerializer
from commons import utils


class RateTripRequestSerializer(commonserializer.CommonSerializer):
    tripId = serializers.IntegerField()
    rating = serializers.IntegerField()
    feedback = serializers.CharField(max_length=300)

