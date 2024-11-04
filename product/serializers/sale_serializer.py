from rest_framework import serializers

from base.models import Inventory, Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ["id", "price", "quantity", "product"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        sale = Sale(**validated_data)
        inventory = Inventory.objects.get(product_id=validated_data["product"].id)
        inventory.sold_out = inventory.sold_out + validated_data["quantity"]
        inventory.available_stock = inventory.stock_in - inventory.sold_out
        inventory.save()
        sale.save()
        return sale
