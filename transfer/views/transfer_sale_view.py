from rest_framework import generics

from base.models import TransferSale
from transfer.serializers import TransferSaleSerializer


class TransferSaleList(generics.ListCreateAPIView):
    queryset = TransferSale.objects.all()
    serializer_class = TransferSaleSerializer


class TransferSaleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransferSale.objects.all()
    serializer_class = TransferSaleSerializer
