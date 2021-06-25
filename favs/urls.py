from django.urls import path
from . import views

app_name = "favs"

urlpatterns = [
    path("add/<int:pk>", views.favs_list, name="list"),
    path("toogle/<int:pk>", views.favs_add, name="save"),
]
