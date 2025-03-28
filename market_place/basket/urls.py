from django.urls import path, re_path

from .views import BasketListView, Confirm


app_name = "basket"

urlpatterns = [
    path("", BasketListView.as_view(), name="basket"),
    path(
        "confirm?product-ind=<int:product_ind>/",
        Confirm.as_view(),
        name="basket_confirm",
    ),
]
