from django.urls import path
from categories import views as genre_views

app_name = "genre"

urlpatterns = [
    path("", genre_views.all_genres, name="genre"),
    path("<int:pk>/", genre_views.DetailGenre.as_view(), name="detail"),
]
