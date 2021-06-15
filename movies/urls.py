from django.urls import path
from movies import views as movies_views
import movies

app_name = "movies"

urlpatterns = [
    path("", movies_views.MovieView.as_view(), name="movies"),
    path("<int:pk>", movies_views.MovieDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", movies_views.UpdateMovieView.as_view(), name="edit"),
    path("create", movies_views.CreateMovieView.as_view(), name="create"),
]
