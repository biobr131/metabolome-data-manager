from django.urls import path

from accounts.views.prod import (
    IndexView, UserLoginView, UserHomeView, UserLogoutView, ContactFormView, PrivacyPolicyView,
    UserListView, UserDetailView
)

app_name = "accounts"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("login", UserLoginView.as_view(), name="login"),
    path("home", UserHomeView.as_view(), name="home"),
    path("logout", UserLogoutView.as_view(), name="logout"),
    path("contact", ContactFormView.as_view(), name="contact"),
    path("privacy-policy", PrivacyPolicyView.as_view(), name="privacy_policy"),
    path("api/users", UserListView.as_view(), name="user_list"),
    path("api/user/<str:username>", UserDetailView.as_view(), name="user_detail"),
]
