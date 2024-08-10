
from django.urls import path
from . import views

app_name='docgen'
urlpatterns = [
    path('invoice_pdf/<int:invoice_id>/', views.invoice_pdf, name="invoice_pdf"),
    path('invoice/download/<int:invoice_id>/', views.download_invoice, name='download_invoice'),
     path('invoice/preview_page/<int:invoice_id>/', views.preview_page, name='preview_page'),
]