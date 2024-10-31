from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    View,
)

from .models import Order

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
    def test_func(self):
        user = self.request.user
        if user.is_staff or user.is_authenticated:
            return True

    def get(self, request):
        queryset = (Order.objects.filter(user_id=self.request.user.pk).prefetch_related("status").order_by("-created_at"))
        # queryset = (Order.objects.filter(user_id=self.request.user.pk).order_by("-created_at").select_related("status"))
        context = {
            "name_page": "Мои заказы",
            "object_list": queryset,
        }
        context.update(CATER_GROUP_NAV)

        return render(request, template_name="order_list.html", context=context)

