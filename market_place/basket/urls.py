from django.urls import path, re_path

from .views import (
    BasketListView,
    add_product_to_basket
    # GroupProductListView,
    # TopSellerProductListView,
    # ExtraListView,
    # ProductDetailView,
)
# from .models import Group, Product

app_name = "basket"

urlpatterns = [
    path("", BasketListView.as_view(), name="basket"),
    # path("?user_id=<int:user_id>&product_id=<int:product_id>/", add_product_to_basket, name="add_product_to_basket"),
    path("<int:user_id>/<int:product_id>/", add_product_to_basket, name="add_product_to_basket"),
]
