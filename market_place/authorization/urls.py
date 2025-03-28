from django.contrib.auth.views import LoginView
from django.urls import path

from .views import (
    CustomLoginView,
    LogoutView,
    ProfileDeliveryAddressUpdateView,
    ProfilePhoneUpdateView,
    RegisterView,
    TelegramRegisterView,
    UserEmailUpdateView,
    UserFirstNameUpdateView,
    UserLastNameUpdateView,
    UserNameUpdateView,
    UserDetailsView,
)

app_name = "authorization"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "login/",
        CustomLoginView.as_view(
            template_name="login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "telegram/<str:jwt_token>/",
        TelegramRegisterView.as_view(),
        name="telegram_register",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("users/<int:pk>/", UserDetailsView.as_view(), name="user_details"),
    path(
        "users/<int:pk>?tab=profile&field=delivery-address/",
        ProfileDeliveryAddressUpdateView.as_view(),
        name="profile_delivery_address_update",
    ),
    path(
        "users/<int:pk>?tab=profile&field=phone/",
        ProfilePhoneUpdateView.as_view(),
        name="profile_phone_update",
    ),
    path(
        "users/<int:pk>?tab=user&field=username/",
        UserNameUpdateView.as_view(),
        name="user_username_update",
    ),
    path(
        "users/<int:pk>?tab=user&field=first-name/",
        UserFirstNameUpdateView.as_view(),
        name="user_first_name_update",
    ),
    path(
        "users/<int:pk>?tab=user&field=last-name/",
        UserLastNameUpdateView.as_view(),
        name="user_last_name_update",
    ),
    path(
        "users/<int:pk>?tab=user&field=email/",
        UserEmailUpdateView.as_view(),
        name="user_email_update",
    ),
]
