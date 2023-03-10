from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("recordings/", views.recordings, name="recordings"),
]