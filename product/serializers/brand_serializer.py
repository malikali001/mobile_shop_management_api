from rest_framework import serializers

from base.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["id", "name", "description"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        brand = Brand(**validated_data)
        brand.save()
        return brand
