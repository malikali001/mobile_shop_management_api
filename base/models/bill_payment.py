from django.db import models
from django.utils import timezone

from .bill import Bill
from .custom_user import CustomUser


class BillPayment(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now())
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.bill.source
