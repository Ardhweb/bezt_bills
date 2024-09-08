import os
import sys
print(sys.path)

from api_core.invoiceapi.serializers import InvoiceSerializer , AddInvoiceItemSerializer
# views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from invoicemodule.models import Invoice
from django.shortcuts import get_object_or_404

#Use FBV and CBV Mix And match


#CBV -4 Production  is Good


#Initial High Level  Using FBV
@api_view(['GET'])
def invoice_list(request):
    """
    Retrieve all invoices.
    param: request
    """
    invoices = Invoice.objects.all()
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST', 'GET'])
def invoice_create(request):
    if request.method == 'POST':
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        invoices = Invoice.objects.filter(user=request.user)
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET', 'PUT'])
def invoice_update(request, pk=None):
    if request.method == 'PUT':
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        invoices = Invoice.objects.filter(pk=pk)
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




@api_view(['POST', 'GET'])
def invoice_addnew_item(request, pk):
    if request.method == 'POST':
        invoice = get_object_or_404(Invoice, invoice_id=pk)
        serializer = AddInvoiceItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(invoice=invoice)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        invoices = Invoice.objects.filter(pk=pk)
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




   

'''
@api_view(['POST', 'GET'])
def invoice_addnew_item(request, pk):
    if request.method == "POST":
        try:
            invoice = get_object_or_404(Invoice, invoice_id=pk)
            serializer = AddInvoiceItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(invoice=invoice)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Invoice.DoesNotExist or serializer.errors:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        invoice = Invoice.objects.filter(pk=pk)
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data, status=status.HTTP_200_OK)
'''