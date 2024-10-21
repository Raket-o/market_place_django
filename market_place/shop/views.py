from django.shortcuts import render

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


# ROLE = "marketing"

# class ProductDetailsView(UserPassesTestMixin, DetailView):
class ProductDetailsView(DetailView):
    # def test_func(self):
    #     user = self.request.user
    #     groups = set(str(group) for group in user.groups.all())
    #     if ROLE in groups or user.is_staff:
    #         return True

    template_name = "product_details.html"
    model = Product
    queryset = Product.objects.all()


class ExtraContext(object):
    extra_context = {}
    def get_context_data(self, **kwargs):
        context = super(ExtraContext, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context
class ExtraListView(ExtraContext, ListView):
    pass
class ExtraDetailView(ExtraContext, DetailView):
    pass
class ExtraUpdateView(ExtraContext, UpdateView):
    pass
class ExtraCreateView(ExtraContext, CreateView):
    pass
class ExtraDeleteView(ExtraContext, DeleteView):
    pass
class ExtraCloneView(ExtraUpdateView):
    def post(self, request, *args, **kwargs):
       return ExtraCreateView.as_view(model=self.model,
                              template_name=self.template_name,
                              extra_context=self.extra_context)(request, *args, **kwargs)








from django.shortcuts import render

from shop.models import Category, Group, Product


def index(request):
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

    queryset_top_products = (
        Product.objects
        .filter(archived=False)
        .prefetch_related("group")
        .order_by("-rating")[:10]
    )

    # print(queryset_top_products)

    data = {
        "title": "Хиты продаж",
        "name_page": "Хиты продаж",
        "category_dict": category_dict,
        "top_products": queryset_top_products
    }
    return render(request, "index.html", context=data)




