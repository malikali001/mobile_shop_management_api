from django.db import models

from .product import Product


class Inventory(models.Model):
    product_name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock_in = models.PositiveIntegerField()
    sold_out = models.PositiveIntegerField()
    available_stock = models.PositiveIntegerField()
