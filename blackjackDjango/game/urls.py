from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hit/", views.hit, name="hit"),
    path("stay/", views.stay, name="stay"),
    path("double/", views.double, name="double"),
    path("reset/", views.reset, name="reset"),
]