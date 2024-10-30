from django.contrib import admin

from .models import (
    Bill,
    Brand,
    Category,
    CustomUser,
    Inventory,
    Product,
    Receive,
    Sale,
    Transfer,
    TransferSale,
    BillPayment
)

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Bill)
admin.site.register(BillPayment)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Inventory)
admin.site.register(Product)
admin.site.register(Receive)
admin.site.register(Sale)
admin.site.register(Transfer)
admin.site.register(TransferSale)
