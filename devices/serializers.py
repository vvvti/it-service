from rest_framework import serializers
from . models import Customer, Device, Address, ServiceOrder


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            '__all__'
        )

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = (
            '__all__'
        )

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            '__all__'
        )

class ServiceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceOrder
        fields = (
            '__all__'
        )