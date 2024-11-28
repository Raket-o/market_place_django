import jwt

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_not_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import resolve_url, redirect, render, reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, TemplateView, View
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from jwt.exceptions import InvalidSignatureError

from passlib.context import CryptContext

from .models import Profile

from env_data import algorithm, bot_token
from shop.models import Product
from shop.views import CATER_GROUP_NAV


PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


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


class UserNameUpdateView(UserPassesTestMixin, UpdateView):
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


class ProfileDeliveryAddressUpdateView(UserNameUpdateView):
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


class UserFirstNameUpdateView(UserNameUpdateView):
    model = User
    fields = 'first_name',


class UserLastNameUpdateView(UserNameUpdateView):
    model = User
    fields = 'last_name',


class UserEmailUpdateView(UserNameUpdateView):
    model = User
    fields = 'email',


class TelegramRegisterView(View):
    def get(self, request: HttpRequest, jwt_token: str) -> None:
        payload = jwt.decode(jwt_token, bot_token, algorithms=[algorithm])
        print(type(payload), payload)

        first_name = payload.get("first_name")
        last_name = payload.get("last_name") if payload.get("last_name") else "Не указана"
        messanger = payload.get("messanger")
        messanger_id = payload.get("messanger_id")
        password = PWD_CONTEXT.hash(b"messanger_id")

        user_profile = Profile.objects.filter(messanger_id=messanger_id)
        if not user_profile:
            try:
                user = User(
                    password=password,
                    is_superuser=False,
                    username=messanger_id,
                    first_name=first_name,
                    last_name=last_name,
                    is_staff=False,
                    is_active=True,
                )
                user.save()

                profile = Profile(
                    user_id=user.pk,
                    messanger=messanger,
                    messanger_id=messanger_id,
                )
                profile.save()
                print(profile)
                login(request=request, user=user)


            except AttributeError as err:
                user.delete()
                profile.delete()
                print(err)
        else:
            user_profile = Profile.objects.get(messanger_id=messanger_id)
            user = user_profile.user

        products_list = (
            Product.objects
            .filter(archived=False)
            .prefetch_related("group")
            .order_by("-rating")[:10]
        )

        context = {
            "name_page": "Хиты продаж",
            "object_list": products_list,
            "user": user,
        }

        context.update(CATER_GROUP_NAV)
        response = render(request, 'shop_products_list.html', context=context)
        login(request=request, user=user)
        return response
