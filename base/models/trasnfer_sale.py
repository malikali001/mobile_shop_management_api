from django.db import models
from django.utils import timezone

from .custom_user import CustomUser
from .transfer import Transfer


class TransferSale(models.Model):
    PAYMENT_TYPE_CHOICE = (("send", "Send"), ("receive", "Receive"))
    transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now())
    payment = models.CharField(
        max_length=10, choices=PAYMENT_TYPE_CHOICE, default="send"
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.transfer.source
