from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hit/", views.hit, name="hit"),
    path("stay/", views.stay, name="stay"),
    path("double/", views.double, name="double"),
    path("reset/", views.reset, name="reset"),
    path("next_round/", views.next_round, name="next_round"),
    path("start_round/", views.start_round, name="start_round"),
]