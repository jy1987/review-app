from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from math import ceil
from . import models
from reviews.forms import CreateReviewForm
from reviews.models import Review


class MovieView(ListView):
    """Movie View Definition"""

    model = models.Movie
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "movies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "More Movies"
        return context


class MovieDetail(DetailView):

    model = models.Movie

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        create = request.GET.get("review")
        movie_pk = self.kwargs["pk"]
        reviews = Review.objects.filter(movie=movie_pk)
        context["review"] = True if create == "create" else False
        if reviews:
            context["reviews"] = reviews
        return self.render_to_response(context)

    # get_context_data를 통해 넣고 싶은 context들을 넣는다.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CreateReviewForm()
        return context


def delete_review(request, review_pk, movie_pk):

    user = request.user
    review = Review.objects.get(pk=review_pk)
    review_user = review.created_by
    if user == review_user:
        review.delete()
        return redirect(reverse("movies:detail", kwargs={"pk": movie_pk}))
    else:
        return redirect(reverse("movies:detail", kwargs={"pk": movie_pk}))


class UpdateMovieView(UpdateView):

    model = models.Movie
    fields = (
        "title",
        "year",
        "rating",
        "genre",
        "director",
        "cast",
    )


class CreateMovieView(CreateView):

    model = models.Movie
    fields = (
        "title",
        "year",
        "rating",
        "genre",
        "director",
        "cast",
    )
