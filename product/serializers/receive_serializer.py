from rest_framework import serializers

from base.models import Receive


class ReceiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receive
        fields = ["id", "price", "quantity", "product"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        receive = Receive(**validated_data)
        receive.save()
        return receive
