from django.shortcuts import render
from django.core.paginator import Paginator
from math import ceil
from . import models


# Create your views here.


def all_books(request):
    page = request.GET.get("page", 1)
    all_books = models.Book.objects.all()
    paginator = Paginator(all_books, 10, orphans=5)
    books = paginator.get_page(page)
    print(vars(books.paginator))
    return render(request, "books/all_books.html", {"books": books})
