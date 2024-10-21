from django.urls import path

from .views import (
    ProductDetailsView,
    ExtraDetailView,
)
from .models import Group, Product


queryset_group = (
    Group.objects
    .prefetch_related("category")
    .order_by("category")
)

category_dict = dict()
for qr in queryset_group:
    category_dict.setdefault(qr.category, [])
    group_list = category_dict[qr.category]
    group_list.append(qr.name)
    category_dict[qr.category] = group_list

data = {
        "category_dict": category_dict,
    }
# print(data)

app_name = "shop"

urlpatterns = [
    # path("", TopProductListView.as_view(), name="shop_list"),
    # path("", index, name="shop_list"),
    # path("create/", AdvertisingCompanyCreateView.as_view(), name="advertising_company_create"),
    # path("<int:pk>/", ProductDetailsView.as_view(), name="product_details"),

    path(
        "<int:pk>/",
        ExtraDetailView.as_view(
            model=Product,
            extra_context=data,
            template_name='product_details.html'
        ),
        name='product_details'
    ),
    # path("<int:pk>/update/", AdvertisingCompanyUpdateView.as_view(), name="advertising_company_update"),
    # path("<int:pk>/delete/", AdvertisingCompanyDeleteView.as_view(), name="advertising_company_archived"),
]
