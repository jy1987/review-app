from django.shortcuts import render, redirect, reverse
from favs import models as favs_model
from movies import models as movies_model
from books import models as books_model

# Create your views here.


def favs_list(request, pk):
    favlist = favs_model.FavList.objects.get(created_by=pk)
    movie_lists = favlist.movies.all()
    book_lists = favlist.books.all()
    return render(
        request,
        "favs.html",
        {"writer": favlist, "movies": movie_lists, "books": book_lists},
    )


def favs_add(request, pk):
    kind = request.GET.get("kind", "movie")
    user = request.user

    if user.is_authenticated:
        fav_list, _ = favs_model.FavList.objects.get_or_create(created_by=user)
        if kind == "movie":
            movie = movies_model.Movie.objects.get(pk=pk)
            if movie in fav_list.movies.all():
                fav_list.movies.remove(movie)
            else:
                fav_list.movies.add(movie)
            fav_list.save()
            return redirect(reverse("movies:detail", kwargs={"pk": pk}))
        else:
            book = books_model.Book.objects.get(pk=pk)
            if book in fav_list.books.all():
                fav_list.books.remove(book)
            else:
                fav_list.books.add(book)
            fav_list.save()
            return redirect(reverse("books:detail", kwargs={"pk": pk}))
