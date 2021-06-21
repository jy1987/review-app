from django.urls import path
from core import views as core_views

app_name = "core"

urlpatterns = [
    path("", core_views.home, name="home"),
    path("search/", core_views.search, name="search"),
    path("search/<int:pk>", core_views.CategorySearch.as_view(), name="detail"),
]
