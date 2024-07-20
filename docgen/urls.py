
from django.urls import path
from . import views

app_name='docgen'
urlpatterns = [
   
    path('generate-pdf/<int:id>/', views.generate_pdf, name="generate-pdf"),
    
]