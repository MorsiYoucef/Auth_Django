from .views import authView,home
from django.contrib.auth import views as auth_views, logout
from django.urls import path,include
from django.contrib.auth.views import LogoutView


urlpatterns = [
     path("", home, name="home"),
     path("logout/",logout, name="logout"),
     path("signup/", authView, name="authView"),
     path("accounts/", include("django.contrib.auth.urls")),

]
