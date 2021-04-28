from rest_framework import routers
from .api import (CustomerViewSet, AddressViewSet, DeviceViewSet, ServiceOrderViewSet)


router = routers.DefaultRouter()
router.register('api/customer', CustomerViewSet, 'customer')
router.register('api/address', AddressViewSet, 'address')
router.register('api/device', DeviceViewSet, 'invoiceposition')
router.register('api/serviceOrder', ServiceOrderViewSet, 'serviceOrder')

urlpatterns = router.urls