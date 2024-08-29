from django.urls import path, include
from .main_routers import router
urlpatterns = [
    path('invoiceapi/', include('api_core.invoiceapi.urls')),  # App1 API
    # Add more as needed
]
urlpatterns += router.urls
