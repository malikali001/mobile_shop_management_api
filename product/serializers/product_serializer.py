from django.core.exceptions import ValidationError
from rest_framework import serializers

from base.models import Inventory, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "category", "brand"]

    def create(self, validated_data):
        try:
            user = self.context["request"].user
            validated_data["user"] = user
            product = Product(**validated_data)
            product.save()

            try:
                inventory = Inventory.objects.create(
                    product_name=validated_data["name"], product=product
                )
                inventory.save()
            except Exception as e:
                product.delete()
                raise ValidationError({"inventory_error": str(e)})

            return product

        except ValidationError as ve:
            raise ve
        except Exception as e:
            raise ValidationError({"error": str(e)})
