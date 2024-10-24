from django.urls import path, re_path

from .views import (
    GroupProductListView,
    TopSellerProductListView,
    ProductDetailView,
)


app_name = "shop"

urlpatterns = [
    # path("", TopProductListView.as_view(), name="shop_list"),
    # path("", index, name="top_products_list"),
    # path("create/", AdvertisingCompanyCreateView.as_view(), name="advertising_company_create"),
    # path("<int:pk>/", ProductDetailsView.as_view(), name="product_details"),

    # path(
    #     "",
    #     ExtraTopSellerProductDetailsView.as_view(),
    #     name='index'
    # ),

    path("", TopSellerProductListView.as_view(), name='index'),
    # re_path(r'^categories/', GroupProductListView.as_view(), name='group_product_list_view'),
    path("categories/<str:category>/groups/<str:group>/", GroupProductListView.as_view(), name='group_product_list_view'),
    path("products/<int:pk>/", ProductDetailView.as_view(), name='product_details'),

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
