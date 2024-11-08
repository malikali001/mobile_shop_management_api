from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from base import permissions
from base.models import BillPayment, TransferSale
from bill.serializers import BillPaymentSerializer
from product.utils import calculate_product, calculate_profit
from transfer.serializers import TransferSaleSerializer


class ProfitCalculation(APIView):
    permission_classes = [permissions.IsAdmin]

    def post(self, request, format=None):
        data = request.data
        try:
            date = data["date"].split("-")
            gross_product_profit, total_sale, total_cost = calculate_product(date)
            transfer_profit = calculate_profit(
                date, TransferSale, TransferSaleSerializer
            )
            bill_profit = calculate_profit(date, BillPayment, BillPaymentSerializer)
        except Exception:
            return Response(
                {"error": "An unexpected error occurred"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        response = {
            "gross_product_profit": gross_product_profit,
            "total_sale": total_sale,
            "total_cost": total_cost,
            "transfer_profit": transfer_profit,
            "bill_profit": bill_profit,
        }
        return Response(response, status=status.HTTP_200_OK)
