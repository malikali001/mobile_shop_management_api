from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from product.views import (
    brand_view,
    category_view,
    inventory_view,
    product_view,
    receive_view,
    sale_view,
)

urlpatterns = [
    path("", product_view.ProductList.as_view()),
    path("<int:pk>", product_view.ProductDetail.as_view()),
    path("brand", brand_view.BrandList.as_view()),
    path("brand/<int:pk>", brand_view.BrandDetail.as_view()),
    path("category", category_view.CategoryList.as_view()),
    path("category/<int:pk>", category_view.CategoryDetail.as_view()),
    path("receive", receive_view.ReceiveList.as_view()),
    path("receive/<int:pk>", receive_view.ReceiveDetail.as_view()),
    path("sale", sale_view.SaleList.as_view()),
    path("sale/<int:pk>", sale_view.SaleDetail.as_view()),
    path("inventory", inventory_view.InventoryList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
