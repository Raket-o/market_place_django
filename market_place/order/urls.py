from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from market_place.settings import CACHE_SECONDS

from .views import (
    OrderListView,
#     TopSellerProductListView,
#     ProductDetailView,
)


app_name = "order"

urlpatterns = [
    path("", OrderListView.as_view(), name="order_list"),
    # path("", index, name="top_products_list"),
    # path("create/", AdvertisingCompanyCreateView.as_view(), name="advertising_company_create"),
    # path("<int:pk>/", ProductDetailsView.as_view(), name="product_details"),

    # path(
    #     "",
    #     ExtraTopSellerProductDetailsView.as_view(),
    #     name='index'
    # ),

    # path("products/top-seller-product/", TopSellerProductListView.as_view(), name='top_seller_product'),
    # path("", cache_page(CACHE_SECONDS)(TopSellerProductListView.as_view()), name='top_seller_product'),
    # path("products?pk=<int:pk>/", cache_page(CACHE_SECONDS)(ProductDetailView.as_view()), name='product_details'),
    # re_path(r'^categories/', GroupProductListView.as_view(), name='group_product_list_view'),
    # path("categories?category=<str:category>&groups=<str:group>/", cache_page(CACHE_SECONDS)(GroupProductListView.as_view()), name='group_product_list_view'),

    # path(
    #     "products/<int:pk>/",
    #     ExtraDetailView.as_view(
    #         model=Product,
    #         extra_context=data,
    #         template_name='product_details.html'
    #     ),
    #     name='product_details'
    # ),
]
