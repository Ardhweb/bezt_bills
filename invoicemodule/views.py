from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
# from .forms import InvoiceForm,InvoiceItemForm ,InvoiceFormSet
from django.urls import reverse
from django.forms.models import (
    inlineformset_factory, 
    formset_factory, 
    modelform_factory, 
    modelformset_factory
)
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .forms import InvoiceForm, InvoiceItemForm, InvoiceFormSet
from .models import Invoice, InvoiceItem

def preselect_template(*args, **kwargs):
    #Return select tempate type
    pass




# Define the formset factory outside the request method
def get_invoice_formset(extra=3):
    return inlineformset_factory(
        Invoice,
        InvoiceItem,
        form=InvoiceItemForm,
        fields=['desc', 'qty', 'price'],
        extra=extra,  # Number of extra forms
        can_delete=True
    )

def add_invoice(request):
    InvoiceFormSet = inlineformset_factory(
        Invoice,
        InvoiceItem,
        form=InvoiceItemForm,
        fields=['desc', 'qty', 'price'],
         
        can_delete=True
    )
    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST)
        
        # # Get total forms count from POST data
        total_forms = int(request.POST.get('invoiceitem_set-TOTAL_FORMS', 1))  # Default to 1 if not present
        
        # # Create the formset with the dynamic number of extra forms
        # InvoiceFormSet = get_invoice_formset(extra=total_forms)
        
        item_formset = InvoiceFormSet(request.POST, instance=None)

        if invoice_form.is_valid() and item_formset.is_valid():
            invoice = invoice_form.save()
            item_formset.instance = invoice
            item_formset.save()
            return redirect(reverse('invoicemodule:render-page', kwargs={'id': invoice.pk}))
        else:
            print("Invoice form errors:", invoice_form.errors)
            print("Item formset errors:", item_formset.errors)
    else:
        invoice_form = InvoiceForm()
        # Create formset with a default number of forms
        InvoiceFormSet = get_invoice_formset(extra=1)
        item_formset = InvoiceFormSet()

    context = {
        'invoice_form': invoice_form,
        'item_formset': item_formset
    }
    return render(request, 'invoice/add_invoice.html', context)






# Make sure you have imported the necessary modules (InvoiceForm, InvoiceFormSet, etc.) correctly.



def homepage(request):
    invoices = Invoice.objects.all()
    context = {
        'invoices':invoices,
    }
    return render(request, 'home.html', context)


def render_page(request, id):
    template_name = 'pretemplate/default.html'
    items = InvoiceItem.objects.filter(invoice__pk=id)
    context = {
        'items':items,
    }
    return render(request, template_name, context)


def delete_item(request, id):
    invoice = Invoice.objects.get(pk=id)
    # Delete all related invoice items
    InvoiceItem.objects.filter(invoice=invoice).delete()
    # Delete the invoice itself
    invoice.delete()
    # Handle successful deletion, e.g., return a success message or redirect
    return redirect('invoicemodule:home')  # Replace with your desired redirect URL


