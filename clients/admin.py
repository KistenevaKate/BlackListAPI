
from django.contrib import admin
from .models import Client, Comment_client, Status_client

@admin.register(Client, Comment_client, Status_client)
class AuthorAdmin(admin.ModelAdmin):
    pass
# Register your models here.
