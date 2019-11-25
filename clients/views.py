from django.shortcuts import render

def clientsView(request):
    return render(request, 'clients/clients.html', {})

def companiesView(request):
    return render(request, 'clients/company.html', {})
# Create your views here.
