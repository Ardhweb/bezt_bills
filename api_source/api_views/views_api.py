from invoicemodule.models import Invoice, InvoiceItem
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db import transaction
@login_required
@require_POST
def delete_invoice_by_user(request, invoice_id):
    try:
        # Use a transaction to ensure atomicity and prevent concurrent modifications
        with transaction.atomic():
            # Retrieve the invoice by ID and lock it for update
            invoice = Invoice.objects.select_for_update().get(pk=invoice_id)

            # Check if the current user is allowed to delete this invoice
            # if invoice.user != request.user:
            #     return JsonResponse({'status': 'failed', 'message': 'Unauthorized'}, status=403)

            # Delete related invoice items
            InvoiceItem.objects.filter(invoice=invoice).delete()

            # Delete the invoice itself
            invoice.delete()

        return JsonResponse({'status': 'success'}, status=200)
    except Invoice.DoesNotExist:
        return JsonResponse({'status': 'failed', 'message': 'Invoice not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'failed', 'message': str(e)}, status=400)