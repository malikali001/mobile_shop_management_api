from rest_framework import serializers

from base.models import Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ["id", "price", "quantity", "product"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        sale = Sale(**validated_data)
        sale.save()
        return sale
