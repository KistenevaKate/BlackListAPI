from django.urls import path

from .views import clientsView, companiesView

urlpatterns = [
    path('clients', clientsView),
    path('company', companiesView)
]