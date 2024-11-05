from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from transfer.views import transfer_sale_view, transfer_view

urlpatterns = [
    path("", transfer_view.TransferList.as_view()),
    path("<int:pk>", transfer_view.TransferDetail.as_view()),
    path("sale", transfer_sale_view.TransferSaleList.as_view()),
    path("sale/<int:pk>", transfer_sale_view.TransferSaleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
