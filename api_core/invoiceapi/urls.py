# urls.py
from django.urls import path
from .views import invoice_create, invoice_list

urlpatterns = [
    path('create-invoice/', invoice_create, name='create-invoice'),
    path('list-invoice/', invoice_list, name='list-invoice'),
]
