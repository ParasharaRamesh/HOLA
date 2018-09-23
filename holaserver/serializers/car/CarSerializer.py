from rest_framework import serializers

class CarSerializer(serializers.Serializer):
    carId = serializers.CharField(max_length=100)
    carType = serializers.CharField(max_length=100)
    carModel = serializers.CharField(max_length=100)
    carLicense = serializers.CharField(max_length=100)


