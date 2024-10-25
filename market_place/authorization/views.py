# from django.contrib.auth import logout
# from django.shortcuts import redirect
# from django.views.generic.base import View
#
#
# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return redirect("authorization:login")

from django.contrib.auth.decorators import login_not_required
from django.utils.decorators import method_decorator


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import resolve_url, redirect, reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, TemplateView, View
from django.urls import reverse_lazy

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


# class CustomLogoutView(LogoutView):
#     template_name = 'authorization/login.html'
#
#     def get_default_redirect_url(self):
#         # return resolve_url('authorization:login')
#         return resolve_url('shop:top_seller_product')

# @method_decorator(login_not_required, name="dispatch")
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


# def set_cookie_view(request: HttpRequest) -> HttpResponse:
#     response = HttpResponse("Cookie set")
#     response.set_cookie(key="new_val", value="Ya tut", max_age=60)
#     return response
#
#
# def get_cookie_view(request: HttpRequest) -> HttpResponse:
#     value = request.COOKIES.get("new_val", "default_value")
#     return HttpResponse(f"Cookie value: {value!r}")
#
#
# def set_session_view(request: HttpRequest) -> HttpResponse:
#     request.session["custom_field"] = "new_value"
#     return HttpResponse("Session set!")
#
#
# def get_session_view(request: HttpRequest) -> HttpResponse:
#     value = request.session.get("custom_field", "default_value")
#     return HttpResponse(f"Session value: {value!r}")


class UsersListView(ListView):
    template_name = "users_list.html"
    queryset = (
        User.objects
        .select_related("profile")
    )


class UserDetailsView(DetailView):
    template_name = "user_details.html"
    queryset = (
        User.objects
        .select_related("profile")
    )


class AboutMeDetailView(TemplateView):
    template_name = "authorization/about_me.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"name_page": "Мой профиль"})
        context.update(CATER_GROUP_NAV)
        return context


# class ProfileUpdateView(UserPassesTestMixin, UpdateView):
class ProfileUpdateView(UpdateView):
    # def test_func(self):
    #     user = self.request.user
    #     return (
    #             user.is_superuser
    #             or user.is_staff
    #             or user.has_perm("authorization.change_profile")
    #             or user.id == self.get_object().user.profile.user.pk
    #     )

    model = Profile
    fields = "delivery_address"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse(
            viewname="authorization:user_details",
            kwargs={"pk": self.object.user.pk},
        )
