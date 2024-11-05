from rest_framework import serializers

from base.models import Transfer


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ["id", "source"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        transfer = Transfer(**validated_data)
        transfer.save()
        return transfer
