from rest_framework import serializers

from base.models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ["id", "product_name", "stock_in", "sold_out", "available_stock"]
