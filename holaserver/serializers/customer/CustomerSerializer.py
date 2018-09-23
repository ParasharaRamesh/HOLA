from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    customerId=serializers.CharField()
    name=serializers.CharField()
    email=serializers.EmailField()
    phone=serializers.CharField()
    pastSevenDaysRideCount=serializers.IntegerField()