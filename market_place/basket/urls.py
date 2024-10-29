from django.urls import path, re_path

from .views import (
    BasketListView,
    Confirm,
#     add_product_cookie_view,
#     add_product_to_basket,
#     # GroupProductListView,
#     # TopSellerProductListView,
#     # ExtraListView,
#     # ProductDetailView,
)
# # from .models import Group, Product
#
app_name = "basket"

urlpatterns = [
    path("", BasketListView.as_view(), name="basket"),
    path("confirm?product-ind=<int:product_ind>/", Confirm.as_view(), name="basket_confirm"),
#     # path("?user_id=<int:user_id>&product_id=<int:product_id>/", add_product_to_basket, name="add_product_to_basket"),
#     # path("<int:user_id>/<int:product_id>/", add_product_to_basket, name="add_product_to_basket"),
#     # path("<int:product_id>/", add_product_cookie_view, name="add_product_to_basket"),
#     path("add/", add_product_cookie_view, name="add_product_to_basket"),
]
