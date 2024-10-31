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
        queryset = (
            Order.objects
            .filter(user_id=self.request.user.pk)
            .prefetch_related("status")
            .order_by("-created_at")
        )
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


class OrderDetails(View):
    # class OrderListView(UserPassesTestMixin, DetailView):
    #     def test_func(self):
    #         user = self.request.user
    #         if user.is_staff or user.is_authenticated:
    #             return True

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        # queryset = (Profile.objects.filter(user_id=self.request.user.pk).prefetch_related("user").first())
        queryset = (Order.objects.filter(id=pk).first())
        # print("OrderDetails(get)=queryset====", queryset)
        products_str = str(queryset.products).split("|")

        product_list = []
        for prod in products_str:
            print(prod)

            # i = i[1:-1]
            prod = prod.split(", ")
            print(prod)
            product = CustomProductClass(*prod)
            product_list.append(product)

        print(product_list[0].id)
        print(product_list[0].name)
        print(product_list[0].price)
        print(product_list[0].size)
        print(product_list[0].color)
        print(product_list[0].photo)


        context = {
            "name_page": f"Детали заказа № {pk}",
            "object": queryset,
            "object_list": product_list,
            # "total_price": total_price,
        }
        context.update(CATER_GROUP_NAV)
        return render(request, template_name="order_details.html", context=context)

    # def post(self, request: HttpRequest) -> HttpResponse:
    #     from .models import Product as CustomClassProduct, Status
    #
    #     status = Status.objects.get(id=1)
    #     # print("OrderArrange(post)=====")
    #
    #     value = request.COOKIES.get("basket")
    #     products_id = f"{value}"
    #     product_id_list = products_id.split(" ")
    #
    #     total_price = 0
    #     products_list = []
    #     # orders_list = []
    #     for product_id in product_id_list[1:]:
    #         product = Product.objects.get(id=product_id)
    #         name = product.name
    #         size = product.size
    #         color = product.color
    #         price = product.price
    #         photo = product.photo
    #         custom_class_product = CustomClassProduct(
    #             name, size, color, price, photo
    #         )
    #         products_list.append(str(custom_class_product))
    #         # print("OrderArrange(post)=products_list====", custom_class_product)
    #         # order_obj = Order(user=self.request.user, status=status, products=product, price=product.price)
    #         # orders_list.append(order_obj)
    #         total_price += product.price
    #
    #     print("OrderArrange(post)=products_list====", products_list)
    #     # print("OrderArrange(post)=products_list====",str(products_list))
    #     # print("OrderArrange(post)=order_obj====",order_obj)
    #
    #     order_obj = Order(user=self.request.user, status=status, products="|".join(products_list), price=total_price)
    #     order_obj.save()
    #     # print("OrderArrange(post)=order_obj====",order_obj.__dict__)
    #
    #     queryset = (
    #         Order.objects
    #         .filter(user_id=self.request.user.pk)
    #         .prefetch_related("status")
    #         .order_by("-created_at"))
    #
    #     context = {
    #         "name_page": "Мои заказы",
    #         "object_list": queryset,
    #         "total_price": total_price,
    #     }
    #     context.update(CATER_GROUP_NAV)
    #     response = render(request, template_name="order_list.html", context=context)
    #     # response.delete_cookie('basket')
    #     return response

