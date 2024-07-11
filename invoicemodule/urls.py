
from django.urls import path
from . import views

app_name='invoicemodule'
urlpatterns = [
    path('', views.homepage, name="home"),
    path('add-invoice', views.add_invoice, name="add-invoice"),
    
]