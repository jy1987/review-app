from django.shortcuts import render
from django.core.paginator import Paginator
from math import ceil
from . import models


# Create your views here.


def all_movies(request):
    page = request.GET.get("page", 1)
    all_movies = models.Movie.objects.all()
    paginator = Paginator(all_movies, 10, orphans=5)
    movies = paginator.get_page(page)
    print(vars(movies.paginator))
    return render(request, "movies/all_movies.html", {"movies": movies})
