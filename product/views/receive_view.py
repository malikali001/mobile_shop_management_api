from rest_framework import generics

from base.models import Receive
from product.serializers import ReceiveSerializer


class ReceiveList(generics.ListCreateAPIView):
    queryset = Receive.objects.all()
    serializer_class = ReceiveSerializer


class ReceiveDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receive.objects.all()
    serializer_class = ReceiveSerializer
