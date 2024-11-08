from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from base.models import Inventory, Product, Receive


class ReceiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receive
        fields = ["id", "price", "quantity", "product"]

    def create(self, validated_data):
        try:
            user = self.context["request"].user
            validated_data["user"] = user

            receive = Receive(**validated_data)

            try:
                inventory = Inventory.objects.get(
                    product_id=validated_data["product"].id
                )
                inventory.stock_in += validated_data["quantity"]
                inventory.available_stock += validated_data["quantity"]
            except ObjectDoesNotExist:
                raise ValidationError(
                    {"inventory": "Inventory record for this product does not exist."}
                )

            try:
                product = Product.objects.get(pk=validated_data["product"].id)
                product.price = validated_data["price"]
            except ObjectDoesNotExist:
                raise ValidationError(
                    {"product": "The specified product does not exist."}
                )

            product.save()
            receive.save()
            inventory.save()

            return receive

        except ValidationError as ve:
            raise ve
        except Exception as e:
            raise ValidationError({"error": str(e)})
