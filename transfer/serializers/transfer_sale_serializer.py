from rest_framework import serializers
from base.models import TransferSale


class TransferSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferSale
        fields = [
            "id",
            "amount",
            "commission",
            "payment",
            "transfer"
        ]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        transfer_sale = TransferSale(**validated_data)
        transfer_sale.save()
        return transfer_sale
