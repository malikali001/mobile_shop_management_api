from rest_framework import serializers

from base.models import BillPayment


class BillPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillPayment
        fields = ["id", "amount", "commission", "bill"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        bill_payment = BillPayment(**validated_data)
        bill_payment.save()
        return bill_payment
