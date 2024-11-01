from django.urls import path

from .views import (
    OrderArrange,
    OrderDetails,
    OrderListView,
)


app_name = "order"

urlpatterns = [
    path("", OrderListView.as_view(), name="order_list"),
    path("&order-id=<int:pk>", OrderDetails.as_view(), name="order_details"),
    path("arrange/", OrderArrange.as_view(), name="order_arrange"),
]
