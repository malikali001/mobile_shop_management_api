from django.db import models

from .product import Product


class Inventory(models.Model):
    product_name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock_in = models.PositiveIntegerField(blank=True, null=True, default=0)
    sold_out = models.PositiveIntegerField(blank=True, null=True, default=0)
    available_stock = models.PositiveIntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.product_name
