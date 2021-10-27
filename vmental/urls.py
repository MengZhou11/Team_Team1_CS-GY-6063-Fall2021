from django.conf.urls import include, url
from django.urls import path
from . import views
from vmental.views import IndexView, activate, signup


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("auth/", include("django.contrib.auth.urls")),
    path("auth/signup/", signup, name="signup"),
    path("activate/<uidb64>/<token>/", activate, name="activate"),
]
