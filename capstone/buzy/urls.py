from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("create", views.create, name="create"),
    path("edit/<int:id>", views.create, name="edit"),
    path("profile",views.profile, name="profile"),
    path("project/<int:id>", views.project, name="project"),
]