from django.conf import settings
from django.db import models
from django.utils import timezone

 
class Client(models.Model):
    fio = models.CharField(max_length=35)
    telephone = models.CharField(max_length = 15)
    email = models.EmailField(max_length=254) 
    status_client= models.ForeignKey( 'Status_client', on_delete=models.CASCADE, )
    create_date = models.DateField(auto_now_add=True)
    descriptions = models.CharField(max_length = 500)

    class Meta:
        verbose_name_plural ="Клиенты"
        verbose_name = "Клиент"

class Status_client(models.Model):
    name = models.CharField(max_length = 35)
    description = models.CharField(max_length = 500)
    color = models.IntegerField()

    class Meta:
        verbose_name_plural ="Статусы клиентов"
        verbose_name = "Статус клиента"

class Comment_client(models.Model):
    client=models.ForeignKey( 'Client', on_delete=models.CASCADE, )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length = 500)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural ="Статусы клиентов"
        verbose_name = "Статус клиента"


