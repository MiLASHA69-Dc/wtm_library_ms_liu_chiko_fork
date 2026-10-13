from django.urls import path
from .views import registration_view, login_view, logout_view, userprofile_view

app_name = "accounts"
urlpatterns = [
    # path("",home_page,name="index"),
    path("register-page/",registration_view,name="registration"),
    path("login-page/",login_view,name="login"),
    path("My-Profile/",userprofile_view,name="user_profile"),
    path("logout/",logout_view,name="logout"),
]
