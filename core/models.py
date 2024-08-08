from django.db import models

# Create your models here.
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Address(BaseModel):
    ADDRESS_TYPE_ROLE = (
        ('invoicer','Invoicer'),
        ('customer', 'Customer'),
    )
    lane_1 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=50, blank=True)
    country =  models.CharField(max_length=50, blank=True)
    address_type = models.CharField(max_length=50, blank=True, choices=ADDRESS_TYPE_ROLE)
    to_billing = models.BooleanField(default=False)
    to_shipping = models.BooleanField(default=False)
    to_permanent= models.BooleanField(default=False)
    #invoice_fk = models.ForeignKey("invoicemodule.Invoice", on_delete=models.CASCADE)