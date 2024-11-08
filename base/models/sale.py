from django.db import models
from django.utils import timezone

from .custom_user import CustomUser
from .product import Product


class Sale(models.Model):
    date = models.DateTimeField(default=timezone.now())
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.PositiveIntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
