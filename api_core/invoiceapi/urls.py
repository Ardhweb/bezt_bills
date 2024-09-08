# urls.py
from django.urls import path
from .views import invoice_update,invoice_create, invoice_list,invoice_addnew_item

urlpatterns = [
    path('update-invoice/<int:pk>/', invoice_update, name='update-invoice'),
    path('additem-invoice/<int:pk>/', invoice_addnew_item, name='additem-invoice'),
    path('create-invoice/', invoice_create, name='create-invoice'),
    path('list-invoice/', invoice_list, name='list-invoice'),
]
