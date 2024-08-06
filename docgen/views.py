from django.shortcuts import render ,get_object_or_404
from  invoicemodule.models import Invoice, InvoiceItem
from django.http import HttpResponse
from django.utils import timezone
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
# Create your views here.
# @staff_member_required
def invoice_pdf(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    items =   InvoiceItem.objects.filter(invoice=invoice)
    template_name_with_location = 'default/invoice/invo_temp/default_invoice_template.html'

    html = render_to_string(f'{template_name_with_location}',
    {'invoice': invoice,'items':items,})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=o_{invoice.pk}.pdf'
    weasyprint.HTML(string=html).write_pdf(response)
    # weasyprint.HTML(string=html).write_pdf(response,stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
    return response

