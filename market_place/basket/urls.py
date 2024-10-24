from django.urls import path, re_path

# from .views import (
    # GroupProductListView,
    # TopSellerProductListView,
    # ExtraListView,
    # ProductDetailView,
# )
# from .models import Group, Product


# queryset_group = (
#     Group.objects
#     .prefetch_related("category")
#     .order_by("category")
# )
#
# category_dict = dict()
# for qr in queryset_group:
#     category_dict.setdefault(qr.category, [])
#     group_list = category_dict[qr.category]
#     group_list.append(qr.name)
#     category_dict[qr.category] = group_list
#
# data = {
#         "category_dict": category_dict,
#     }
# # print(data)

app_name = "basket"

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

    # path("", TopSellerProductListView.as_view(), name='index'),
    # path("categories/Мужская обувь/", TopSellerProductListView.as_view(), name='group_product_list_view'),
    # re_path(r'^categories/', GroupProductListView.as_view(), name='group_product_list_view'),
    # path("categories/<str: category>/groups/<str: group>/", GroupProductListView.as_view(), name='group_product_list_view'),
    # path("categories/<str:category>/groups/<str:group>/", GroupProductListView.as_view(), name='group_product_list_view'),
    # path("categories/<str:category>/groups/", GroupProductListView.as_view(), name='group_product_list_view'),
    # path("categories/Мужская обувь/", TopSellerProductListView.as_view(), name='group_product_list_view'),
    # path("categories/%D0%9C%D1%83%D0%B6%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D1%83%D0%B2%D1%8C/groups/", TopSellerProductListView.as_view(), name='group_product_list_view'),
# categories/%D0%9C%D1%83%D0%B6%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D1%83%D0%B2%D1%8C/groups/%D1%81%D0%BF%D1%80%D0%BE%D1%82%D0%B8%D0%B2%D0%BD%D0%B0%D1%8F
#     path("products/<int:pk>/", ProductDetailView.as_view(), name='product_details'),

    # path(
    #     "products/<int:pk>/",
    #     ExtraDetailView.as_view(
    #         model=Product,
    #         extra_context=data,
    #         template_name='product_details.html'
    #     ),
    #     name='product_details'
    # ),


    # path("<int:pk>/update/", AdvertisingCompanyUpdateView.as_view(), name="advertising_company_update"),
    # path("<int:pk>/delete/", AdvertisingCompanyDeleteView.as_view(), name="advertising_company_archived"),
]
