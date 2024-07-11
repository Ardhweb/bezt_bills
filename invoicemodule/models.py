from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    random_invoice_id = models.CharField(max_length=250, blank=True, null=True)
    template_name =  models.CharField(max_length=250, blank=True, null=True)
    #date = models.DateField(auto_now=True, null=True, blank=True, editable=True)
    user = models.ForeignKey(User,  on_delete=models.SET_NULL, null=True)
    INVOICE_STATUS = (
        ('Pending','Pending'),
        ('Paid','Paid'),
        ('Done','Done'),
    )
    status = models.CharField(max_length=255, choices=INVOICE_STATUS,  null=True)


class InvoiceItem(models.Model):
    desc =  models.CharField(max_length=250, blank=True, null=True)
    qty = models.PositiveIntegerField(db_column='quntity')
    price =  models.CharField(max_length=250, blank=True, null=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True)

