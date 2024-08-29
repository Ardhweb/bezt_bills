import os
import sys
print(sys.path)

from api_core.invoiceapi.serializers import InvoiceSerializer
# views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from invoicemodule.models import Invoice

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
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)