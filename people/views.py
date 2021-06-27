from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.shortcuts import render
from django.core.paginator import Paginator
from math import ceil
from . import models


# Create your views here.


class PeopleView(ListView):
    """Movie View Definition"""

    model = models.Person
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "people"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "More People"
        return context


class PeopleDetail(DetailView):
    model = models.Person


class UpdatePeopleView(UpdateView):

    model = models.Person
    fields = (
        "name",
        "kind",
    )


class CreatePeopleView(CreateView):

    model = models.Person
    fields = (
        "name",
        "kind",
    )
