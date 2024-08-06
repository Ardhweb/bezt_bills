
from django.urls import path
from . import views

app_name='docgen'
urlpatterns = [
    path('invoice_pdf/<int:invoice_id>/', views.invoice_pdf, name="invoice_pdf"),
]