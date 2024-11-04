from rest_framework import generics, mixins

from base.models import Inventory
from product.serializers import InventorySerializer


class InventoryList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
