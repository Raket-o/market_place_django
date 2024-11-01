from django.urls import path
from django.views.decorators.cache import cache_page
from market_place.settings import CACHE_SECONDS

from .views import (
    GroupProductListView,
    TopSellerProductListView,
    ProductDetailView,
)


app_name = "shop"

urlpatterns = [
    path("", cache_page(CACHE_SECONDS)(TopSellerProductListView.as_view()), name='top_seller_product'),
    path("products?pk=<int:pk>/", cache_page(CACHE_SECONDS)(ProductDetailView.as_view()), name='product_details'),
    path("categories?category=<str:category>&groups=<str:group>/", cache_page(CACHE_SECONDS)(GroupProductListView.as_view()), name='group_product_list_view'),
]
