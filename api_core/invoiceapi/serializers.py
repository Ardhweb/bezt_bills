from rest_framework import serializers
from invoicemodule.models import Invoice, InvoiceItem, Invoicer
from django.db import transaction

class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ['desc', 'qty', 'price']

class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True)
    class Meta:
        model = Invoice
        fields = ['date','status' ,'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')  # Extract and remove 'items' from the validated data
        invoice = Invoice.objects.create(**validated_data)  # Create the Order instance
    
        # Prepare OrderItem instances
        invoice_items = [
            InvoiceItem(invoice=invoice, **item_data) for item_data in items_data
        ]
    
        # Define a reasonable batch size
        batch_size = 1000
        total_items = len(invoice_items)
    
        with transaction.atomic():  # Ensure all-or-nothing transaction
            for i in range(0, total_items, batch_size):
                chunk = invoice_items[i:i + batch_size]
                InvoiceItem.objects.bulk_create(chunk)
    
        return invoice

