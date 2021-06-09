from django.shortcuts import render
from . import models

# Create your views here.


def all_genres(request):

    all_genres = models.Genre.objects.all()
    return render(request, "genres/all_genres.html", context={"genres": all_genres})
