# serializers.py
from rest_framework import serializers
from .models import GpsData

class GpsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GpsData
        fields = ['message', 'timestamp']
