from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField
from commons.serializers import commonserializer
from commons.serializers.entities.trip import TripSerializer
from commons.datatypes.entities.trip import PaymentMode, CompleteTripTransactionStatus
from commons import utils


class CompleteTripRequestSerializer(commonserializer.CommonSerializer):
    tripId = serializers.IntegerField()
    completeTripOption = serializers.IntegerField()
    finishLocation = PointField()
    paymentMode = serializers.ChoiceField(choices=utils.enumTuples(PaymentMode))


class CompleteTripResponseSerializer(commonserializer.CommonSerializer):
        completeTripStatus = serializers.ChoiceField(choices=utils.enumTuples(CompleteTripTransactionStatus))
        trip = TripSerializer()
