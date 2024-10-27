from django.views.generic import (
    # CreateView,
    # DeleteView,
    # DetailView,
    ListView,
    # UpdateView,
)

from .models import Basket
from shop.views import CATER_GROUP_NAV

from shop.models import Group, Product


class BasketListView(ListView):
    template_name = "basket_products_list.html"
    # queryset = Basket.objects.filter(id=1)
    # queryset = Basket.objects.all()
    # print(queryset)

    # total_price = 0
    # for obj_basket in queryset:
    #     total_price += obj_basket.product.price
        # print(obj_basket.product.price)

    def get_queryset(self):
        user = self.request.user
        print("get_queryset+++++++++++++++++++++++========", user)

        queryset = Basket.objects.filter(user_id=user.id)
        self.total_price = 0
        for obj_basket in queryset:
            self.total_price += obj_basket.product.price

        print("queryset=================", queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context.update(CATER_GROUP_NAV)
        context.update({"name_page": "Корзина", "total_price": self.total_price})
        # context.update({"name_page": "Корзина", "total_price": 0})
        return context


# class BasketCreateView(PermissionRequiredMixin, CreateView):
# class BasketCreateView(CreateView):
#     # permission_required = "shopapp.add_product"
#
#     model = Basket
#     fields = "name", "price", "description", "discount"
#     success_url = reverse_lazy("shopapp:products_list")
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         response = super().form_valid(form)
#         return response


from django.shortcuts import render


def add_product_to_basket(request, user_id: int, product_id: int):
    print("add_product_to_basket+++++++++++++++++++++++========")
    print(request)
    print(user_id)
    print(product_id)
    print()


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

    # queryset = (
    #     Product.objects
    #     .filter(archived=False)
    #     .prefetch_related("group")
    #     .order_by("-rating")[:10]
    # )
    add_product = Basket(user_id=user_id, product_id=product_id)
    print(add_product)
    add_product.save()

    queryset = (
        Basket.objects
        .filter(user_id=user_id)
        # .prefetch_related("group")
        # .order_by("-rating")[:10]
    )

    total_price = 0
    for obj_basket in queryset:
        total_price += obj_basket.product.price

    data = {
        "title": "Корзина",
        "name_page": "Корзина",
        "category_dict": category_dict,
        "object_list": queryset,
        "total_price": total_price,
    }

    print("queryset=================", queryset)
    return render(request, "basket_products_list.html", context=data)
    # return render(request, "shop_products_list.html", context=data)
