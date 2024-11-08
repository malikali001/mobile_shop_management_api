from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from base.models import Inventory, Product, Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ["id", "price", "cost_price", "quantity", "product"]

    def create(self, validated_data):
        try:
            user = self.context["request"].user
            validated_data["user"] = user

            try:
                product = Product.objects.get(pk=validated_data["product"].id)
                validated_data["cost_price"] = product.price
            except ObjectDoesNotExist:
                raise ValidationError(
                    {"product": "The specified product does not exist."}
                )

            sale = Sale(**validated_data)

            try:
                inventory = Inventory.objects.get(
                    product_id=validated_data["product"].id
                )
                inventory.sold_out += validated_data["quantity"]
                inventory.available_stock = inventory.stock_in - inventory.sold_out
                inventory.save()
            except ObjectDoesNotExist:
                raise ValidationError(
                    {"inventory": "Inventory record for this product does not exist."}
                )

            sale.save()
            return sale

        except ValidationError as ve:
            raise ve
        except Exception as e:
            raise ValidationError({"error": str(e)})
