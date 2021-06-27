from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from math import ceil
from . import models
from reviews.forms import CreateReviewForm
from reviews.models import Review


# Create your views here.


class BookView(ListView):
    """Movie View Definition"""

    model = models.Book
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "More Books"
        return context


class BookDetail(DetailView):

    model = models.Book

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        create = request.GET.get("review")
        book_pk = self.kwargs["pk"]
        reviews = Review.objects.filter(book=book_pk)
        context["review"] = True if create == "create" else False
        if reviews:
            context["reviews"] = reviews
        return self.render_to_response(context)

    # get_context_data를 통해 넣고 싶은 context들을 넣는다.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CreateReviewForm()
        return context


def delete_review(request, review_pk, book_pk):

    user = request.user
    review = Review.objects.get(pk=review_pk)
    review_user = review.created_by
    if user == review_user:
        review.delete()
        return redirect(reverse("books:detail", kwargs={"pk": book_pk}))
    else:
        return redirect(reverse("books:detail", kwargs={"pk": book_pk}))


class UpdateBookView(UpdateView):

    model = models.Book
    fields = (
        "title",
        "year",
        "rating",
        "genre",
        "writer",
    )


class CreateBookView(CreateView):

    model = models.Book
    fields = (
        "title",
        "year",
        "rating",
        "genre",
        "writer",
    )
