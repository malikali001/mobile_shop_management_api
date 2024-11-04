from rest_framework import serializers

from base.models import Inventory, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "category", "brand"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        product = Product(**validated_data)
        product.save()
        inventory = Inventory.objects.create(
            product_name=validated_data["name"],
            product=product,
            stock_in=0,
            sold_out=0,
            available_stock=0,
        )
        inventory.save()
        return product
