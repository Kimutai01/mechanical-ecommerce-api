from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.products import products
from base.models import PaymentResponse
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes

from base.serializer import PaymentResponseSerializer
from rest_framework import status


@api_view(['POST'])
def createPaymentResponse(request):
    data = request.data
    print('Data:', data)
    try:
        if data['Success'] == True:

            payment = PaymentResponse.objects.create(
                Message=data['Message'],
                Success=data['Success'],
                Status=data['Status'],
                Amount=data['Amount'],
                transaction_code=data['transaction_code'],
                transaction_reference=data['transaction_reference'],

            )
        else:

            payment = PaymentResponse.objects.create(
                Message=data['Message'],
                Success=data['Success'],
                Status=data['Status'],
                transaction_reference=data['transaction_reference'],

            )

        serializer = PaymentResponseSerializer(payment, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except KeyError as e:
        return Response({'error': f'Missing key: {e}'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getPaymentResponse(request):
    paymentResponse = PaymentResponse.objects.all()
    serializer = PaymentResponseSerializer(paymentResponse, many=True)
    return Response(serializer.data)
