from django.urls import path

from .views import (
    # AdvertisingCompaniesListView,
    # AdvertisingCompanyCreateView,
    # AdvertisingCompanyDeleteView,
    # AdvertisingCompanyDetailsView,
    # AdvertisingCompanyUpdateView,
    # AdvertisingCompanyViewSet,
    TopProductListView,
    index,
)

app_name = "shop"

urlpatterns = [
    # path("", TopProductListView.as_view(), name="shop_list"),
    # path("", index, name="shop_list"),
    # path("create/", AdvertisingCompanyCreateView.as_view(), name="advertising_company_create"),
    # path("<int:pk>/", AdvertisingCompanyDetailsView.as_view(), name="advertising_company_details"),
    # path("<int:pk>/update/", AdvertisingCompanyUpdateView.as_view(), name="advertising_company_update"),
    # path("<int:pk>/delete/", AdvertisingCompanyDeleteView.as_view(), name="advertising_company_archived"),
]
