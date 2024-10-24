from django.urls import path, re_path

from .views import (
    BasketListView,
    # GroupProductListView,
    # TopSellerProductListView,
    # ExtraListView,
    # ProductDetailView,
)
# from .models import Group, Product

app_name = "basket"

urlpatterns = [
    path("", BasketListView.as_view(), name="basket"),
]
