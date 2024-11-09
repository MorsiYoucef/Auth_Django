from .views import authView,home
from django.urls import path,include


urlpatterns = [
     path("signup/", authView, name="authView"),
     path("", home, name="home"),
     path("accounts/", include("django.contrib.auth.urls")),
]
