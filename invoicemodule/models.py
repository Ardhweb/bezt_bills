from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone

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
    due_date = models.DateField(auto_now=True)
    expire_date = models.DateField(auto_now=True)
    mark_delete = models.BooleanField(default=False)



class InvoiceItem(BaseModel):
    desc =  models.CharField(max_length=250, blank=True, null=True)
    qty = models.PositiveIntegerField(db_column='quntity')
    price =  models.CharField(max_length=250, blank=True, null=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True)

