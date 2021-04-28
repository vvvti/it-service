from .models import Customer, Device, Address, ServiceOrder
from rest_framework import viewsets, permissions
from .serializers import AddressSerializer, CustomerSerializer, DeviceSerializer, ServiceOrderSerializer



class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    
    serializer_class = CustomerSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    
    serializer_class = DeviceSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AddressSerializer

class ServiceOrderViewSet(viewsets.ModelViewSet):
    queryset = ServiceOrder.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ServiceOrderSerializer