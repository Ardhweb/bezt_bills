from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Invoice
# Create your views here.
from .forms import InvoiceForm,InvoiceItemForm, InvoiceFormSet
def preselect_template(*args, **kwargs):
    #Return select tempate type
    pass

def add_invoice(request,*args, **kwargs):
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        invoice = Invoice.objects.get(pk=5)
        formset = InvoiceFormSet(request.POST, instance=invoice)
        print(formset)
        
        if formset.is_valid() and form.is_valid:
            instance = form.save()
            formset.instance = instance
            formset.save()
            return redirect('invoicemodule:home')
    else:
        invoice_form = InvoiceForm()
        item_formset = InvoiceFormSet()  
    context = {
    'invoice_form': invoice_form,
    'item_formset': item_formset,}
    return render(request, 'invoice/add_invoice.html', context)

# Make sure you have imported the necessary modules (InvoiceForm, InvoiceFormSet, etc.) correctly.



def homepage(request):
    return render(request, 'home.html')
