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
    template_name = 'top_products_list.html'
    queryset = (
        Product.objects
        .filter(archived=False)
        .prefetch_related("group")
        .order_by("-rating")[:10]
    )

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context.update(CATER_GROUP_NAV)
        return context


class GroupProductListView(ListView):
    model = Product
    template_name = 'group_products_list.html'
    # queryset = (
    #     Product.objects
    #     .filter(group=False)
    #     .prefetch_related("group")
    # )

    # def get_queryset(self):
    #     url = self.request.__dict__
    #     # url = self.request.GET.__dict__
    #     # url = self.request.REQUEST_METHOD.GET.PATH_INFO
    #     from pprint import pprint
    #     print("=+"*50, type(url), url)
    #     return (
    #     Product.objects
    #     .filter(group=False)
    #     .prefetch_related("group")
    # )

    def get(self, request, *args, **kwargs):
        # either
        # self.object_list = self.get_queryset()
        # self.object_list = self.url
        self.object_list = request

        print("==========================", self.object_list)
        # print("==========================", str(self.object_list).encode("UTF-8"))
        # print("==========================", self.get_context_data())
        # print("==========================", *args, **kwargs)

        # self.object_list = self.object_list.filter(lab__acronym=kwargs['lab'])

        # or
        # queryset = Lab.objects.filter(acronym=kwargs['lab'])
        # if queryset.exists():
        #     self.object_list = self.object_list.filter(lab__acronym=kwargs['lab'])
        # else:
        #     raise Http404("No lab found for this acronym")
        #
        # # in both cases
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context.update(CATER_GROUP_NAV)
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_details.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context.update(CATER_GROUP_NAV)
        return context




from django.shortcuts import render
def index(request):
    # print(request)

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

    queryset_top_products = (
        Product.objects
        .filter(group=False)
        .prefetch_related("group")
        .order_by("-rating")[:10]
    )

    data = {
        "title": "Хиты продаж",
        "name_page": "Хиты продаж",
        "category_dict": category_dict,
        "top_products": queryset_top_products
    }
    return render(request, "index.html", context=data)



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
