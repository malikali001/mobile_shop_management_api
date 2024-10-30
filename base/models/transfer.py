from django.db import models

from .custom_user import CustomUser


class Transfer(models.Model):
    source = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.source
