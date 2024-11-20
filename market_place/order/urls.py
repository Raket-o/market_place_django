from django.urls import path

from .views import (
    Confirm,
    OrderArrange,
    OrderDetails,
    OrderListView,
)


app_name = "order"

urlpatterns = [
    path("", OrderListView.as_view(), name="order_list"),
    path("<int:pk>", OrderDetails.as_view(), name="order_details"),
    path("arrange/", OrderArrange.as_view(), name="order_arrange"),
    path("confirm?order-id=<int:pk>/", Confirm.as_view(), name="order_confirm"),
]
