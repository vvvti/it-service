from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    first_name = models.CharField("Imię", max_length=20)
    sure_name = models.CharField("Nazwisko", max_length=20)    
    email = models.EmailField("Adres email")
    telephone_number = models.CharField("Numer telefonu", max_length=20)
    is_active = models.BooleanField
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Klient"
        verbose_name_plural = "Klienci"

    def __str__(self):
        return str(self.sure_name)
    

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    city = models.CharField("Miasto", max_length=60)
    street = models.CharField("Ulica", max_length=140)
    number = models.CharField("Numer", max_length=20)
    postal_code = models.CharField("Kod pocztowy", max_length=20)
    post = models.CharField("Poczta", max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Adres"
        verbose_name_plural = "Adresy"

    def __str__(self):
        return str(self.street)



class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    device_type = models.CharField("Rodzaj urządzenia", max_length=160)
    device_name = models.CharField("Nazwa urzadzenia", max_length=160)
    serial_number = models.CharField("Numer seryjny", max_length=160)
    is_active = models.BooleanField
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Urządzenie"
        verbose_name_plural = "Urządzenia"

    def __str__(self):
        return str(self.serial_number)


class ServiceOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    date = models.DateTimeField('Data złożenia')
    description = models.CharField('Opis', max_length=1000)
    is_active = models.BooleanField
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Zlecenie naprawy"
        verbose_name_plural = "Zlecenia naprawy"

    def __str__(self):
        return str(self.device)