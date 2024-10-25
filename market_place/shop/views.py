from django.db import connection
# from django.shortcuts import render

# from django.contrib.auth.mixins import UserPassesTestMixin
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import OrderingFilter, SearchFilter
# from rest_framework import viewsets
# from django.shortcuts import reverse
# from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Category, Group, Product
from django.db.utils import ProgrammingError

# ROLE = "marketing"
try:
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

except ProgrammingError:
    pass

CATER_GROUP_NAV = {"category_dict": category_dict}


# class ExtraContext(object):
#     extra_context = {}
#
#     def get_context_data(self, **kwargs):
#         context = super(ExtraContext, self).get_context_data(**kwargs)
#         context.update(self.extra_context)
#         return context
#
#
# class ExtraListView(ExtraContext, ListView):
#     pass
#
#
# class ExtraDetailView(ExtraContext, DetailView):
#     pass
#
#
# class ExtraUpdateView(ExtraContext, UpdateView):
#     pass
#
#
# class ExtraCreateView(ExtraContext, CreateView):
#     pass
#
#
# class ExtraDeleteView(ExtraContext, DeleteView):
#     pass


class TopSellerProductListView(ListView):
    model = Product
    template_name = "shop_products_list.html"
    queryset = (
        Product.objects
        .filter(archived=False)
        .prefetch_related("group")
        .order_by("-rating")[:10]
    )

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context.update(CATER_GROUP_NAV)
        context.update({"name_page": "Хиты продаж"})
        return context


class GroupProductListView(ListView):
    model = Product
    template_name = "shop_products_list.html"

    def get(self, request, *args, **kwargs):
        self.category = kwargs["category"]
        self.group = kwargs["group"]
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(
                    self.object_list, "exists"
            ):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(
                    _("Empty list and “%(class_name)s.allow_empty” is False.")
                    % {
                        "class_name": self.__class__.__name__,
                    }
                )
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_queryset(self):
        sql_query = f"""
        SELECT sp.id, sp.name, sp.price, sp.photo
        FROM shop_product as sp
        JOIN shop_product_group spg on sp.id = spg.product_id
        JOIN shop_group sg on sg.id = spg.group_id
        JOIN shop_category sc on sc.id = sg.category_id
        WHERE sc.name = '{self.category}' AND sg.name = '{self.group}';
            """

        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            results = cursor.fetchall()

        class Photo:
            def __init__(self, name: str, url: str):
                self.name = name
                self.url = url

        class Product:
            def __init__(self, id: int, name: str, price: str, photo: Photo):
                self.id = id
                self.name = name
                self.price = price
                self.photo = photo

        product_list = []
        for attrs in results:
            id, name, price, photo_url = attrs
            photo = Photo(name, f"/media/{photo_url}")
            product = Product(id, name, price, photo)
            product_list.append(product)
        return product_list

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context.update(CATER_GROUP_NAV)
        context.update({"name_page": self.group})
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "shop_product_details.html"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context.update(CATER_GROUP_NAV)
        return context


# from django.shortcuts import render
#
#
# def index(request):
#     # print(request)
#
#     queryset_group = (
#         Group.objects
#         .prefetch_related("category")
#         .order_by("category")
#     )
#
#     category_dict = dict()
#     for qr in queryset_group:
#         category_dict.setdefault(qr.category, [])
#         group_list = category_dict[qr.category]
#         group_list.append(qr.name)
#         category_dict[qr.category] = group_list
#
#     queryset_top_products = (
#         Product.objects
#         .filter(group=False)
#         .prefetch_related("group")
#         .order_by("-rating")[:10]
#     )
#
#     data = {
#         "title": "Хиты продаж",
#         "name_page": "Хиты продаж",
#         "category_dict": category_dict,
#         "top_products": queryset_top_products
#     }
#     return render(request, "index.html", context=data)

# class ExtraCloneView(ExtraUpdateView):
#     def post(self, request, *args, **kwargs):
#         return ExtraCreateView.as_view(model=self.model,
#                                        template_name=self.template_name,
#                                        extra_context=self.extra_context)(request, *args, **kwargs)


# class ExtraListView(ExtraUpdateView):
#     def post(self, request, *args, **kwargs):
#         return ExtraCreateView.as_view(model=self.model,
#                                        template_name=self.template_name,
#                                        extra_context=self.extra_context)(request, *args, **kwargs)