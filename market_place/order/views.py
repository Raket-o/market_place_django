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

from .models import Order, CustomProductClass, Status
from .utils import send_message_tg

from env_data import live_cookies
from authorization.models import Profile
from shop.models import Product
from shop.views import CATER_GROUP_NAV


class OrderListView(UserPassesTestMixin, View):
    def test_func(self) -> bool:
        user = self.request.user
        if user.is_staff or user.is_authenticated:
            return True

    def get(self, request: HttpRequest) -> HttpResponse:
        queryset = (
            Order.objects
            .filter(user_id=self.request.user.pk)
            .prefetch_related("status")
            .order_by("-created_at")
        )
        context = {
            "name_page": "Мои заказы",
            "object_list": queryset,
        }
        context.update(CATER_GROUP_NAV)

        return render(request, template_name="order_list.html", context=context)


class OrderArrange(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        queryset = (Profile.objects.filter(user_id=self.request.user.pk).prefetch_related("user").first())

        value = request.COOKIES.get("basket")
        products_id = f"{value}"
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
        status = Status.objects.get(id=1)
        value = request.COOKIES.get("basket")
        products_id = f"{value}"
        product_id_list = products_id.split(" ")

        total_price = 0
        products_list = []
        for product_id in product_id_list[1:]:
            product = Product.objects.get(id=product_id)
            id = product_id
            name = product.name
            price = product.price
            size = product.size
            color = product.color
            photo = f"/static/media/{product.photo}"
            custom_product_class = CustomProductClass(
                id, name, price, size, color, photo
            )
            products_list.append(str(custom_product_class))
            total_price += product.price

        order_obj = Order(
            user=self.request.user,
            status=status,
            products="|".join(products_list),
            total_price=total_price
        )
        order_obj.save()
        send_message_tg(order_obj.id)

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
        response = render(request, template_name="order_list.html", context=context)
        response.delete_cookie('basket')
        return response


class OrderDetails(UserPassesTestMixin, View):
    def test_func(self) -> bool:
        user = self.request.user
        if user.is_staff or user.is_authenticated:
            return True

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        queryset = (Order.objects.filter(id=pk).first())
        products_str = str(queryset.products).split("|")

        product_list = []
        for prod in products_str:
            prod = prod.split(", ")
            product = CustomProductClass(*prod)
            product_list.append(product)

        context = {
            "name_page": f"Детали заказа № {pk}",
            "object": queryset,
            "object_list": product_list,
        }
        context.update(CATER_GROUP_NAV)
        return render(request, template_name="order_details.html", context=context)
