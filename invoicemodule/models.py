from django.db import models
from core.models import BaseModel,Address
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone

class Invoicer(BaseModel):
    company_name =  models.CharField(max_length=250, blank=True, null=True)
    origin_address = models.ForeignKey(Address,  on_delete=models.CASCADE, null=True)
  

class Invoice(BaseModel):
    invoice_id = models.AutoField(primary_key=True)
    random_invoice_id = models.CharField(max_length=250, blank=True, null=True)
    template_name =  models.CharField(max_length=250, blank=True, null=True)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User,  on_delete=models.SET_NULL, null=True)
    INVOICE_STATUS = (
        ('Pending','Pending'),
        ('Paid','Paid'),
        ('Done','Done'),
        ('Expired','Expired'),
    )
    status = models.CharField(max_length=255, choices=INVOICE_STATUS,  null=True)
    due_date = models.DateField(blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
    mark_delete = models.BooleanField(default=False)
    billing_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    shipping_address = models.ForeignKey(Address,related_name="ship_address", on_delete=models.CASCADE, null=True)
    invoicer = models.ForeignKey(Invoicer, on_delete=models.SET_NULL, null=True)



class InvoiceItem(BaseModel):
    desc =  models.CharField(max_length=250, blank=True, null=True)
    qty = models.PositiveIntegerField(db_column='quntity')
    price =  models.CharField(max_length=250, blank=True, null=True)
    invoice = models.ForeignKey(Invoice, related_name='items' ,on_delete=models.SET_NULL, null=True)



