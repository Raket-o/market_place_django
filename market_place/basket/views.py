from django.views.generic import (
    # CreateView,
    # DeleteView,
    # DetailView,
    ListView,
    # UpdateView,
)

from .models import Basket
from shop.views import CATER_GROUP_NAV


class BasketListView(ListView):
    template_name = "basket_products_list.html"
    # queryset = Basket.objects.filter(id=1)
    queryset = Basket.objects.all()
    # print(queryset)

    total_price = 0
    for obj_basket in queryset:
        total_price += obj_basket.product.price
        print(obj_basket.product.price)

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context.update(CATER_GROUP_NAV)
        context.update({"name_page": "Корзина", "total_price": self.total_price})
        return context
