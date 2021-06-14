from django.urls import path
from movies import views as movies_views
import movies

app_name = "movies"

urlpatterns = [
    path("", movies_views.MovieView.as_view(), name="movies"),
    path("<int:pk>", movies_views.MovieDetail.as_view(), name="detail"),
]
