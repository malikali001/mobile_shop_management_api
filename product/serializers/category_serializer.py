from rest_framework import serializers

from base.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        category = Category(**validated_data)
        category.save()
        return category
