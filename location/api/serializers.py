from rest_framework import serializers
from location.models import Location

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ['lat','lon','description','category', ]

class LocationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ['point','description','category','user']
