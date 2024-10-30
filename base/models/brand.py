from django.db import models

from .custom_user import CustomUser


class Brand(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
