from django.shortcuts import render
from .models import Clients

def clientsView(request):
    clients = Clients.objects.all()
    return render(request, 'clients/clients.html', {'clients':clients})

def companiesView(request):
    return render(request, 'clients/company.html', {})
# Create your views here.
