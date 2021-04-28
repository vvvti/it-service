from django.contrib import admin
from . models import Customer, Address, Device, ServiceOrder

admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Device)
admin.site.register(ServiceOrder)