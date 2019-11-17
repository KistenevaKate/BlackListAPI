from django.contrib import admin

from .models import Clients
from .models import Phone
from .models import ClientsPhone

class ClientAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName')
    list_display_links = ('firstName', 'lastName')
    search_fields = ('title', 'content')

admin.site.register(Clients, ClientAdmin)
admin.site.register(Phone)
admin.site.register(ClientsPhone)
# Register your models here.
