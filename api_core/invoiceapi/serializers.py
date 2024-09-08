from rest_framework import serializers
from invoicemodule.models import Invoice, InvoiceItem, Invoicer
from django.db import transaction
from rest_framework.exceptions import ValidationError


class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ['desc', 'qty', 'price']

class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['date', 'status', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')  # Extract and remove 'items' from the validated data
        invoice, created = Invoice.objects.get_or_create(**validated_data)  # Get or create the Invoice instance

        # Prepare InvoiceItem instances
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

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', None)  # Extract items data
        existing_items = instance.items.all()  # Fetch existing items

        # Update invoice fields
        for field in validated_data:
            if getattr(instance, field) != validated_data[field]:
                setattr(instance, field, validated_data[field])
        instance.save()

        if items_data is not None:
            item_ids = {item['id'] for item in items_data if 'id' in item}

            # Identify items to delete (those not in incoming data)
            items_to_delete = [item for item in existing_items if item.id not in item_ids]

            # Prepare items to create or update
            items_to_create = []
            items_to_update = []

            for item_data in items_data:
                if 'id' in item_data:
                    item_instance = next((item for item in existing_items if item.id == item_data['id']), None)
                    if item_instance:
                        # Update existing item if needed
                        if any(getattr(item_instance, field) != item_data[field] for field in item_data):
                            for field in item_data:
                                setattr(item_instance, field, item_data[field])
                            items_to_update.append(item_instance)
                    else:
                        raise ValidationError(f"Invoice item with id {item_data['id']} does not exist.")
                else:
                    # Add new items
                    items_to_create.append(InvoiceItem(invoice=instance, **item_data))

            # Transaction management and batch processing
            batch_size = 1000
            with transaction.atomic():
                # Delete items
                if items_to_delete:
                    for item in items_to_delete:
                        item.delete()

                # Bulk update existing items
                if items_to_update:
                    InvoiceItem.objects.bulk_update(items_to_update, [field for field in items_data[0] if field != 'id'], batch_size=batch_size)

                # Bulk create new items
                if items_to_create:
                    InvoiceItem.objects.bulk_create(items_to_create, batch_size=batch_size)

        return instance


""""
For edit , add new items to  existising invoice we create this new serializer

"""

class AddInvoiceItemSerializer(serializers.ModelSerializer):
    #invoice_id = serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all(), source='invoice')
    class Meta:
        model = InvoiceItem
        fields = ['desc', 'qty', 'price']

    def create(self, validated_data):
        return InvoiceItem.objects.create(**validated_data)
    