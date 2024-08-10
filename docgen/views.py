from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, reverse, render
from  invoicemodule.models import Invoice, InvoiceItem
from django.utils import timezone
from django.conf import settings
from django.template.loader import render_to_string
import weasyprint
from weasyprint import HTML
import os
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate
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


#This func do  alot of indention  so  do  not  tweaks it  make it copy  and save it   backup  the n do  tweaks  at your  copy ok
def download_invoice(request, invoice_id):
    if request.user.is_authenticated:
        success_url = reverse('docgen:preview_page', args=[invoice_id])
        # Retrieve the invoice and related items
        invoice = get_object_or_404(Invoice, pk=invoice_id)
        items = InvoiceItem.objects.filter(invoice=invoice)
    
        # Render the HTML content using the specified template
        template_name_with_location = 'default/invoice/invo_temp/default_invoice_template.html'
        html = render_to_string(template_name_with_location, {'invoice': invoice, 'items': items})
    
        # Define a file path for the PDF in the media directory
        pdf_file_relative_path = f'invoice_{invoice.pk}.pdf'
        pdf_file_path = os.path.join(settings.MEDIA_ROOT, pdf_file_relative_path)
    
        # Ensure the directory exists
        os.makedirs(os.path.dirname(pdf_file_path), exist_ok=True)
    
        # Generate the PDF and save it to the file path
        HTML(string=html).write_pdf(pdf_file_path)
        # Serve the file as a downloadable response
        fs = FileSystemStorage()
        if fs.exists(pdf_file_relative_path):
            with fs.open(pdf_file_relative_path) as pdf_file:
                response = HttpResponse(pdf_file, content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="invoice_{invoice.pk}.pdf"'
    
                # Optionally, clean up the file after serving
                # os.remove(pdf_file_path)
    
                return response
        else:
            # Handle the case where the file was not found
            return HttpResponse("The requested file was not found.", status=404)
        return HttpResponseRedirect(success_url)
    else:
        return HttpResponse("The user was not found.", status=404)
    # Optionally, redirect to another view after the successful generation of the PDF
    # success_url = reverse('docgen:preview_page', args=[invoice_id])
    # return HttpResponseRedirect(success_url)



def preview_page(request, invoice_id):
    context ={
        'invoice_id':invoice_id
    }
    return render(request,'default/preview_page.html', context)
