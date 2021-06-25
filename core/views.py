import categories
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.core.paginator import EmptyPage, Paginator
from movies import models as movie_models
from books import models as book_models
from people import models as people_models
from categories.models import Category, Genre

# Create your views here.


def home(request):

    all_movies = movie_models.Movie.objects.all().order_by("pk")
    paginator_movie = Paginator(all_movies, 10, orphans=5)
    page = request.GET.get("page1", 1)
    try:
        movies = paginator_movie.get_page(page)
    except EmptyPage:
        movies = paginator_movie.get_page(1)

    all_books = book_models.Book.objects.all().order_by("pk")
    paginator_book = Paginator(all_books, 10, orphans=5)
    page = request.GET.get("page2", 1)
    try:
        books = paginator_book.get_page(page)
    except EmptyPage:
        books = paginator_book.get_page(1)

    all_people = people_models.Person.objects.all().order_by("pk")
    paginator_people = Paginator(all_people, 10, orphans=5)
    page = request.GET.get("page3", 1)
    try:
        people = paginator_people.get_page(page)
    except EmptyPage:
        people = paginator_people.get_page(1)

    print(books.object_list)

    return render(
        request,
        "home.html",
        {"movies": movies, "books": books, "people": people, "page_title": "Home!!!"},
    )


def search(request):
    name = request.GET.get("name", "anything")
    name = str(name)
    people = people_models.Person.objects.filter(name__contains=name)
    movies = movie_models.Movie.objects.filter(title__contains=name)
    books = book_models.Book.objects.filter(title__contains=name)
    return render(
        request,
        "search.html",
        {
            "genres": Genre.objects.all(),
            "name": name,
            "people": people,
            "movies": movies,
            "books": books,
        },
    )
