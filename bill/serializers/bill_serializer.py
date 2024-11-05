from rest_framework import serializers

from base.models import Bill


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ["id", "source"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        bill = Bill(**validated_data)
        bill.save()
        return bill
