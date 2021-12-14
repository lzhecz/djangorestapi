from rest_framework import serializers
from .models import Driver, Vehicle


class DriverSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format = '%d/%m/%Y %H:%M:%S', required = False)
    updated_at = serializers.DateTimeField(format = '%d/%m/%Y %H:%M:%S', required = False)

    class Meta:
        model = Driver
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format = '%d/%m/%Y %H:%M:%S', required = False)
    updated_at = serializers.DateTimeField(format = '%d/%m/%Y %H:%M:%S', required = False)

    class Meta:
        model = Vehicle
        fields = '__all__'


class VDSerializer(serializers.Serializer):
    driver = serializers.PrimaryKeyRelatedField(queryset = Driver.objects.all(), allow_null = True)
