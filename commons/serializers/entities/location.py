from rest_framework import serializers
from commons.serializers import commonserializer


class GeoLocationSerializer(commonserializer.CommonSerializer):
    latitude = serializers.FloatField(min_value=-90, max_value=90)
    longitude = serializers.FloatField(min_value=-180, max_value=180)
