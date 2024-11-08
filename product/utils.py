import datetime

from base.models import Sale
from product.serializers import SaleSerializer


def calculate_product(date):
    total_sale = 0
    total_cost = 0
    sale_queryset = Sale.objects.filter(
        date__gte=datetime.date(int(date[0]), int(date[1]), int(date[2]))
    )
    sale_serializer = SaleSerializer(sale_queryset, many=True)
    for item in sale_serializer.data:
        total_sale += float(item["price"]) * item["quantity"]
        total_cost += float(item["cost_price"]) * item["quantity"]

    gross_profit = total_sale - total_cost
    return gross_profit, total_sale, total_cost


def calculate_profit(date, model, serializer):
    profit = 0
    transfer_queryset = model.objects.filter(
        date__gte=datetime.date(int(date[0]), int(date[1]), int(date[2]))
    )
    serializer = serializer(transfer_queryset, many=True)
    profit = sum(map(lambda item: float(item["commission"]), serializer.data))
    return profit
