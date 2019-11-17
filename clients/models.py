from django.conf import settings
from django.db import models
from django.utils import timezone

class Clients(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    about = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.firstName + " " + self.lastName
    
    class Meta:
        verbose_name_plural ="Клиенты"
        verbose_name = "Клиент"

class Phone(models.Model):
    phone = models.CharField(max_length=100) 
   
    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name_plural ="Номера телефонов"
        verbose_name = "Номер телефона"

class ClientsPhone(models.Model):
    clients = models.ForeignKey(Clients, on_delete=models.CASCADE)
    phone =  models.ForeignKey(Phone, on_delete=models.CASCADE)

    def __str__(self):
        return self.clients.firstName + " " + self.clients.lastName+ " " + self.phone.phone

    class Meta:
        verbose_name_plural ="Номера клиентов"
        verbose_name = "Номер клиента"