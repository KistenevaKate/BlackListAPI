from django.shortcuts import render
from .models import Client

def clientsView(request):
	clients = Client.objects.all()
	return render(request, 'clients/clients.html', {'clients':clients})

def companiesView(request):
    return render(request, 'clients/company.html', {})
# Create your views here.
