from django.db import models

from .custom_user import CustomUser


class Bill(models.Model):
    source = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
