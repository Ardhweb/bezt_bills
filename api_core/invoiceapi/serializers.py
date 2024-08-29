from rest_framework import serializers
from invoicemodule.models import Invoice, InvoiceItem, Invoicer

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
