from django.conf import settings
from django.db import models
from django.utils import timezone

class Clients(models.Model):

    
    class Meta:
        verbose_name_plural ="Клиенты"
        verbose_name = "Клиент"