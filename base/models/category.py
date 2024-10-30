from django.db import models

from .custom_user import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
