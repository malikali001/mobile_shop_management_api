from rest_framework import generics

from base.models import BillPayment
from bill.serializers import BillPaymentSerializer


class BillPaymentList(generics.ListCreateAPIView):
    queryset = BillPayment.objects.all()
    serializer_class = BillPaymentSerializer


class BillPaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BillPayment.objects.all()
    serializer_class = BillPaymentSerializer
