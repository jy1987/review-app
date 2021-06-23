from django.shortcuts import render
from django.views.generic import DetailView
from . import models

# Create your views here.


def all_genres(request):

    all_genres = models.Genre.objects.all()
    return render(request, "genres/all_genres.html", context={"genres": all_genres})


class DetailGenre(DetailView):

    model = models.Genre
    context_object_name = "genre"
    template_name = "genres/genre_detail.html"
