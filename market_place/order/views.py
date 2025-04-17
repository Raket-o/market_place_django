from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, reverse
from django.views.generic import ListView, View

from .models import Order, CustomProductClass, Status
from .utils import send_message_tg

from env_data import live_cookies
from authorization.models import Profile
from shop.models import Product
from shop.views import CATER_GROUP_NAV


class OrderListView(UserPassesTestMixin, ListView):
    model = Order
    template_name = "order_list.html"
    paginate_by = 10

    def test_func(self) -> bool:
        user = self.request.user
        if user.is_staff or user.is_authenticated:
            return True

    def get_paginate_by(self, queryset):
        """
        Paginate by specified value in querystring, or use default class property value.
        """
        return self.request.GET.get("paginate_by", self.paginate_by)

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
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

    def get_queryset(self) -> list[Product]:
        return (
            Order.objects.filter(user_id=self.request.user.pk)
            .prefetch_related("status")
            .order_by("-created_at")
        )

    def get_context_data(self, **kwargs) -> dict:
        context = super(ListView, self).get_context_data(**kwargs)
        context.update(CATER_GROUP_NAV)
        context.update({"name_page": "Мои заказы"})
        return context


class OrderArrange(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        queryset = (
            Profile.objects.filter(user_id=self.request.user.pk)
            .prefetch_related("user")
            .first()
        )

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
            photo = f"/media/{product.photo}"
            custom_product_class = CustomProductClass(
                id, name, price, size, color, photo
            )
            products_list.append(str(custom_product_class))
            total_price += product.price

        order_obj = Order(
            user=self.request.user,
            status=status,
            products="|".join(products_list),
            total_price=total_price,
        )
        order_obj.save()
        send_message_tg(order_obj.id)

        queryset = (
            Order.objects.filter(user_id=self.request.user.pk)
            .prefetch_related("status")
            .order_by("-created_at")
        )

        context = {
            "name_page": "Мои заказы",
            "object_list": queryset,
            "total_price": total_price,
        }
        context.update(CATER_GROUP_NAV)
        response = render(request, template_name="order_list.html", context=context)
        response.delete_cookie("basket")
        return response


class OrderDetails(UserPassesTestMixin, View):
    def test_func(self) -> bool:
        user = self.request.user
        if user.is_staff or user.is_authenticated:
            return True

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        queryset = Order.objects.filter(id=pk).first()
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
