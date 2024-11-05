from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from bill.views import bill_payment_view, bill_view

urlpatterns = [
    path("", bill_view.BillList.as_view()),
    path("<int:pk>", bill_view.BillDetail.as_view()),
    path("payment", bill_payment_view.BillPaymentList.as_view()),
    path("payment/<int:pk>", bill_payment_view.BillPaymentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
