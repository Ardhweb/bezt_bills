from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Invoice, InvoiceItem
# Create your views here.
from .forms import InvoiceForm,InvoiceItemForm, InvoiceFormSet
from django.urls import reverse

def preselect_template(*args, **kwargs):
    #Return select tempate type
    pass

# def add_invoice(request,*args, **kwargs):
#     if request.method == "POST":
#         form = InvoiceForm(request.POST)
#         #invoice = Invoice.objects.get(pk=5)
#         formset = InvoiceFormSet(request.POST, instance=form)
#         print(formset)
        
#         if formset.is_valid() and form.is_valid:
#             instance = form.save()
#             formset.instance = instance
#             formset.save()
#             url = reverse('render-page', kwargs={'id':instance.pk})
#             #return redirect('invoicemodule:home')
#             return redirect(url)
#     else:
#         invoice_form = InvoiceForm()
#         item_formset = InvoiceFormSet()  
#     context = {
#     'invoice_form': invoice_form,
#     'item_formset': item_formset,}
#     return render(request, 'invoice/add_invoice.html', context)

def add_invoice(request, *args, **kwargs):
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        formset = InvoiceFormSet(request.POST)

        if formset.is_valid() and form.is_valid():
            instance = form.save()
            formset.instance = instance
            formset.save()
            url = reverse('invoicemodule:render-page', kwargs={'id': instance.pk})
            return redirect(url)
        else:
            context = {'invoice_form': form, 'item_formset': formset}
            return render(request, 'invoice/add_invoice.html', context)
    else:
        invoice_form = InvoiceForm()
        item_formset = InvoiceFormSet()
        context = {'invoice_form': invoice_form, 'item_formset': item_formset}
        return render(request, 'invoice/add_invoice.html', context)


# Make sure you have imported the necessary modules (InvoiceForm, InvoiceFormSet, etc.) correctly.



def homepage(request):
    return render(request, 'home.html')


def render_page(request, id):
    template_name = 'pretemplate/default.html'
    items = InvoiceItem.objects.filter(invoice__pk=id)
    context = {
        'items':items,
    }
    return render(request, template_name, context)
