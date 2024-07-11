from django import forms
from .models import Invoice, InvoiceItem
from django.forms import inlineformset_factory
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
InvoiceFormSet = inlineformset_factory(Invoice, InvoiceItem ,form=InvoiceItemForm,  fields = ['desc', 'qty', 'price']  ,fk_name="invoice",extra=1, can_delete = False)
