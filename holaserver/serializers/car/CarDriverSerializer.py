from rest_framework import serializers

class CarDriverSerializer(serializers.Serializer):
    driverId = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=100)
    rating = serializers.FloatField(min_value=0.0,max_value=5.0)
    feedbacks = serializers.ListField(child=serializers.CharField(max_length=100))

