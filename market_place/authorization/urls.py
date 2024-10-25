# from django.contrib.auth.views import LoginView
# from django.urls import path
#
# from .views import LogoutView
#
# app_name = "authorization"
#
# urlpatterns = [
#     path(
#         "",
#         LoginView.as_view(
#             template_name='authorization/login.html',
#             redirect_authenticated_user=True,
#         ),
#         name="login"
#     ),
#     path("logout/", LogoutView.as_view(), name="logout"),
# ]


from django.contrib.auth.views import LoginView
from django.urls import path

from .views import (
    # get_cookie_view,
    # set_cookie_view,
    # get_session_view,
    # set_session_view,
    AboutMeDetailView,
    CustomLoginView,
    # CustomLogoutView,
    LogoutView,
    ProfileUpdateView,
    RegisterView,
    UserDetailsView,
    UsersListView,
)

app_name = "authorization"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "login/",
        # LoginView.as_view(
        CustomLoginView.as_view(
            template_name='authorization/login.html',
            redirect_authenticated_user=True,
        ),
        name="login"
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("my-profile/", AboutMeDetailView.as_view(), name="my-profile"),
    # path("users/", UsersListView.as_view(), name="users_list"),
    # path("users/<int:pk>/profile/", UserDetailsView.as_view(), name="user_details"),
    # path("users/<int:pk>/update/", ProfileUpdateView.as_view(), name="user_update"),

]
