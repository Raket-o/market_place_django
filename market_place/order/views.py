from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    View,
)

from .models import Order

from env_data import live_cookies
from authorization.models import Profile
from shop.models import Product
from shop.views import CATER_GROUP_NAV


# class OrderListView(ListView):
#     model = Order
#     template_name = "order_list.html"
#     queryset = (
#         Order.objects
#         .filter(user=1)
#         # .prefetch_related("group")
#     )

# class OrderListView(ListView):
#     template_name = "order_list.html"
#     queryset = (
#         Order.objects
#         .select_related("user")
#         .prefetch_related("products")
#     )
#
#     def get_context_data(self, **kwargs):
#         context = super(ListView, self).get_context_data(**kwargs)
#         context.update(CATER_GROUP_NAV)
#         context.update({"name_page": "Мои заказы"})
#         return context


# class OrderListView(ListView):
#     template_name = "order_list.html"
#     queryset = (
#         Order.objects
#         .select_related("user")
#         .prefetch_related("products")
#     )




class OrderListView(UserPassesTestMixin, View):
# class OrderListView(UserPassesTestMixin, DetailView):
    def test_func(self) -> bool:
        user = self.request.user
        if user.is_staff or user.is_authenticated:
            return True

    def get(self, request: HttpRequest) -> HttpResponse:
        queryset = (Order.objects.filter(user_id=self.request.user.pk).prefetch_related("status").order_by("-created_at"))
        # queryset = (Order.objects.filter(user_id=self.request.user.pk).order_by("-created_at").select_related("status"))
        context = {
            "name_page": "Мои заказы",
            "object_list": queryset,
        }
        context.update(CATER_GROUP_NAV)

        return render(request, template_name="order_list.html", context=context)


class OrderArrange(View):
# class OrderListView(UserPassesTestMixin, DetailView):
#     def test_func(self):
#         user = self.request.user
#         if user.is_staff or user.is_authenticated:
#             return True

    def get(self, request: HttpRequest) -> HttpResponse:
        queryset = (Profile.objects.filter(user_id=self.request.user.pk).prefetch_related("user").first())

        value = request.COOKIES.get("basket")
        products_id = f"{value}"
        print("OrderArrange(get)=products_id====", products_id)

        product_id_list = products_id.split(" ")

        total_price = 0
        for product_id in product_id_list[1:]:
            product = Product.objects.get(id=product_id)
            total_price += product.price

        context = {
            "name_page": "Оформление",
            "object": queryset,
            "total_price": total_price,
        }
        context.update(CATER_GROUP_NAV)
        return render(request, template_name="order_form.html", context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        print("OrderArrange(post)=====")

        value = request.COOKIES.get("basket")
        products_id = f"{value}"
        product_id_list = products_id.split(" ")

        total_price = 0
        products_list = []
        for product_id in product_id_list[1:]:
            product = Product.objects.get(id=product_id)
            products_list.append(product)
            total_price += product.price


        # queryset = (
        #     Order.objects
        #     .filter(archived=False)
        #     .prefetch_related("group")
        #     .order_by("-rating")[:10]
        # )

        queryset = (
            Order.objects
            .filter(user_id=self.request.user.pk)
            .prefetch_related("status")
            .order_by("-created_at"))

        context = {
            "name_page": "Мои заказы",
            "object_list": queryset,
            "total_price": total_price,
        }
        context.update(CATER_GROUP_NAV)
        # response = render(request, 'basket_products_list.html', context=context)
        response = render(request, template_name="order_list.html", context=context)
        # products_id = " ".join(product_id_list)
        # response.set_cookie(key="basket", value=products_id, max_age=live_cookies)
        response.delete_cookie('basket')
        # print("ProductDetailView(post)=products_id====", products_id)
        return response


        # queryset = (Order.objects.filter(user_id=self.request.user.pk).prefetch_related("status").order_by("-created_at"))
        # # queryset = (Order.objects.filter(user_id=self.request.user.pk).order_by("-created_at").select_related("status"))
        # context = {
        #     "name_page": "Мои заказы",
        #     "object_list": queryset,
        # }
        # context.update(CATER_GROUP_NAV)
        #
        # return render(request, template_name="order_list.html", context=context)



