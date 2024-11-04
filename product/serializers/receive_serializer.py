from rest_framework import serializers

from base.models import Inventory, Product, Receive


class ReceiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receive
        fields = ["id", "price", "quantity", "product"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        receive = Receive(**validated_data)

        inventory = Inventory.objects.get(product_id=validated_data["product"].id)
        inventory.stock_in = inventory.stock_in + validated_data["quantity"]
        inventory.available_stock = (
            inventory.available_stock + validated_data["quantity"]
        )

        product = Product.objects.get(pk=validated_data["product"].id)
        product.price = validated_data["price"]

        product.save()
        receive.save()
        inventory.save()
        return receive
