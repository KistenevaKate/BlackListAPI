from django.contrib import admin

from .models import Clients
from .models import ContactType
from .models import ClientsContacts

class ClientAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName')
    list_display_links = ('firstName', 'lastName')
    search_fields = ('title', 'content')

admin.site.register(Clients, ClientAdmin)
admin.site.register(ContactType)
admin.site.register(ClientsContacts)
# Register your models here.
