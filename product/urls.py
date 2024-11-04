from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from product.views import brand_view, category_view

urlpatterns = [
    path("brands", brand_view.BrandList.as_view()),
    path("brand/<int:pk>", brand_view.BrandDetail.as_view()),
    path("category", category_view.CategoryList.as_view()),
    path("category/<int:pk>", category_view.CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)