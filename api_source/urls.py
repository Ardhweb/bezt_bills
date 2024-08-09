from django.urls import path, include
from api_source.api_views import views_api

app_name = 'api_source'
urlpatterns = [
    path('delete-invoice-by-user/<int:invoice_id>', views_api.delete_invoice_by_user, name="delete-invoice-by-user"),
]