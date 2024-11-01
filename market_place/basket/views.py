from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from django.views import View
from env_data import live_cookies
from shop.views import CATER_GROUP_NAV
from shop.models import Product


class BasketListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        value = request.COOKIES.get("basket")
        product_id_list = str(value).split(" ")

        total_price = 0
        products_list = []
        for product_id in product_id_list[1:]:
            product = Product.objects.get(id=product_id)
            products_list.append(product)
            total_price += product.price

        context = {
            "name_page": "Корзина",
            "object_list": products_list,
            "total_price": total_price,
        }
        context.update(CATER_GROUP_NAV)
        response = render(request, 'basket_products_list.html', context=context)
        return response


class Confirm(View):
    def get(self, request: HttpRequest, product_ind: int) -> HttpResponse:
        context = {
            "name_page": "Удалить",
        }
        context.update(CATER_GROUP_NAV)
        response = render(request, 'basket_confirm.html', context=context)
        return response

    def post(self, request: HttpRequest, product_ind: int) -> HttpResponse:
        value = request.COOKIES.get("basket")
        products_id = f"{value}"
        product_id_list = products_id.split(" ")
        product_id_list.pop(product_ind)

        total_price = 0
        products_list = []
        for product_id in product_id_list[1:]:
            product = Product.objects.get(id=product_id)
            products_list.append(product)
            total_price += product.price

        context = {
            "name_page": "Корзина",
            "object_list": products_list,
            "total_price": total_price,
        }
        context.update(CATER_GROUP_NAV)
        response = render(request, 'basket_products_list.html', context=context)
        products_id = " ".join(product_id_list)
        response.set_cookie(key="basket", value=products_id, max_age=live_cookies)
        return response
