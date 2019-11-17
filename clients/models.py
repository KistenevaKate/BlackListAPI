from django.conf import settings
from django.db import models
from django.utils import timezone

class Clients(models.Model):
    firstName = models.CharField(max_length=100, verbose_name="Имя")
    lastName = models.CharField(max_length=100, verbose_name="Фамилия")
    phone = models.CharField(null=True, verbose_name="Номер телефона", max_length=20)
    email = models.CharField(null=True, verbose_name="Электронная почта", max_length=50)
    about = models.TextField(verbose_name="Заметка о контакте", null=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Когда создан",)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.firstName + " " + self.lastName
    
    class Meta:
        verbose_name_plural ="Клиенты"
        verbose_name = "Клиент"

class ContactType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    class Meta:
        verbose_name_plural ="Виды контактных данных"
        verbose_name = "Вид контактных данных"

class ClientsContacts(models.Model):
    clients = models.ForeignKey(Clients, on_delete=models.CASCADE)
    contactType =  models.ForeignKey(ContactType, on_delete=models.CASCADE)

    def __str__(self):
        return self.clients.firstName + " " + self.clients.lastName+ " " + self.phone.phone

    class Meta:
        verbose_name_plural ="Доп. контакты клиентов"
        verbose_name = "Доп. контакт клиента"
