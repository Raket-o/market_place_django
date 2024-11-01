from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_not_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import resolve_url, redirect, reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, TemplateView, View
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from .models import Profile

from shop.views import CATER_GROUP_NAV


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "authorization/register.html"
    success_url = reverse_lazy("shop:top_seller_product")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")

        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"name_page": "Регистрация"})
        context.update(CATER_GROUP_NAV)
        return context


class CustomLoginView(LoginView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"name_page": "Вход"})
        context.update(CATER_GROUP_NAV)
        return context


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("shop:top_seller_product")


class UserDetailsView(UserPassesTestMixin, DetailView):
    def test_func(self):
        user = self.request.user
        return (
                user.is_superuser
                or user.is_staff
                or user.id == self.get_object().pk
        )

    template_name = "authorization/profile_details.html"
    queryset = (
        User.objects
        .select_related("profile")
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"name_page": "Мой профиль"})
        context.update(CATER_GROUP_NAV)
        return context


class UserUserNameUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        user = self.request.user
        return (
                user.is_superuser
                or user.is_staff
                or user.id == self.get_object().pk

        )

    model = User
    fields = 'username',
    template_name = "authorization/profile_update_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(CATER_GROUP_NAV)
        return context

    def get_success_url(self):
        return reverse(
            viewname="authorization:user_details",
            kwargs={"pk": self.object.pk},
        )


class ProfileDeliveryAddressUpdateView(UserUserNameUpdateView):
    def test_func(self):
        user = self.request.user
        return (
                user.is_superuser
                or user.is_staff
                or user.id == self.get_object().user.profile.user.pk
        )

    model = Profile
    fields = 'delivery_address',

    def get_success_url(self):
        return reverse(
            viewname="authorization:user_details",
            kwargs={"pk": self.object.user.pk},
        )


class ProfilePhoneUpdateView(ProfileDeliveryAddressUpdateView):
    fields = 'phone_number',

    def get_success_url(self):
        return reverse(
            viewname="authorization:user_details",
            kwargs={"pk": self.object.user.pk},
        )


class UserFirstNameUpdateView(UserUserNameUpdateView):
    model = User
    fields = 'first_name',


class UserLastNameUpdateView(UserUserNameUpdateView):
    model = User
    fields = 'last_name',


class UserEmailUpdateView(UserUserNameUpdateView):
    model = User
    fields = 'email',
