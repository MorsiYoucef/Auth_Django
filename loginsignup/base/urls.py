from .views import authView,home
from django.urls import path,include
from django.contrib.auth.views import LogoutView


urlpatterns = [
     path("", home, name="home"),
     path("signup/", authView, name="authView"),
     path("accounts/", include("django.contrib.auth.urls")),

]
