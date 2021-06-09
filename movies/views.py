from django.shortcuts import render
from . import models

# Create your views here.


def all_movies(request):

    all_movies = models.Movie.objects.all()
    return render(request, "movies/all_movies.html", context={"movies": all_movies})
