from rest_framework import serializers

from base.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "category", "brand"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        product = Product(**validated_data)
        product.save()
        return product
