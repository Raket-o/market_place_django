from django.shortcuts import render

# from django.contrib.auth.mixins import UserPassesTestMixin
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import OrderingFilter, SearchFilter
# from rest_framework import viewsets
# from django.shortcuts import reverse
# from django.urls import reverse_lazy
from django.views.generic import (
    # CreateView,
    # DeleteView,
    # DetailView,
    ListView,
    # UpdateView,
)

from .models import Category, Group, Product
# from .serializers import AdvertisingCompanySerializers
# from utils import HasRolePermission


# ROLE = "marketing"


# class ShopListView(UserPassesTestMixin, ListView):
class TopProductListView(ListView):
    # def test_func(self):
    #     user = self.request.user
    #     groups = set(str(group) for group in user.groups.all())
    #     if ROLE in groups or user.is_staff:
    #         return True

    # permission_required = "advertising_companies.view_advertisingcompany"
    template_name = "top_product_list.html"
    # template_name = "shop/shop_list.html"
    # template_name = "product_list.html"
    queryset = (
        Product.objects
        # .prefetch_related("groups")
        .all()
    )


# from django.shortcuts import render
#
# def index(request):
#     data = {"header": "Hello Django", "message": "Welcome to Python"}
#     # return render(request, "index.html", context=data)
#     return render(request, "shop_list.html", context=data)
