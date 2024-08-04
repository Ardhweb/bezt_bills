from django import forms
from .models import Invoice, InvoiceItem
from django.forms import inlineformset_factory
from django.forms.models import (
    inlineformset_factory, 
    formset_factory, 
    modelform_factory, 
    modelformset_factory
)
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['status',]  # Removed extra space
        widgets ={'status':forms.Select(attrs={'class':'form-control form-select '}),}
class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['desc', 'qty', 'price']  # Removed extra space
        widgets ={'desc':forms.TextInput(attrs={'class':'form-control text-center  '}),
        'qty':forms.TextInput(attrs={'class':'form-control text-center ','type':'number'}),
        'price':forms.TextInput(attrs={'class':'form-control text-center '}),}
InvoiceFormSet = inlineformset_factory(Invoice, InvoiceItem ,form=InvoiceItemForm,fields = ['desc', 'qty', 'price']  ,fk_name="invoice", can_delete = False)
#Remove  extra=1 for saving  mulitple instance
# from django.forms import modelformset_factory

# InvoiceItemFormSet = modelformset_factory(
#     InvoiceItem,
#     form=InvoiceItemForm,
#     fields=['desc', 'qty', 'price'],
#     can_delete=False
# )
