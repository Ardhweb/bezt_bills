from django.shortcuts import render 
from  invoicemodule import models
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.
def generate_pdf(request):
    # Assuming your model is named `MyModel` and has a `user` foreign key
    #last_created_object = Invoice.objects.filter(user=user).latest('created_at')

    return HttpResponse('Ok dude')