from django.shortcuts import render
from . import models

# Create your views here.


def all_books(request):

    all_books = models.Book.objects.all()
    return render(request, "books/all_books.html", context={"books": all_books})
