from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.core.paginator import Paginator
from math import ceil
from . import models


# Create your views here.


class BookView(ListView):
    """Movie View Definition"""

    model = models.Book
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "More Books"
        return context


class BookDetail(DetailView):

    model = models.Book
