from rest_framework import serializers

class EstimateForCarTypeSerializer(serializers.Serializer):
    carType = serializers.CharField(max_length=100)
    tripPrice = serializers.FloatField()

