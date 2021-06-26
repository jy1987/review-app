from core import models
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, reverse
from . import forms
from movies import models as movie_models
from books import models as book_models
from reviews import models as review_models

# Create your views here.
def create_review(request, pk):

    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            form = forms.CreateReviewForm(request.POST)

            if form.is_valid():
                try:
                    movie = movie_models.Movie.objects.get(pk=pk)
                    review = form.save()
                    review.created_by = request.user
                    review.movie = movie
                    review.save()
                    return redirect(reverse("movies:detail", kwargs={"pk": pk}))
                except ObjectDoesNotExist:
                    book = book_models.Book.objects.get(pk=pk)
                    review = form.save()
                    review.created_by = request.user
                    review.book = book
                    review.save()
                    return redirect(reverse("books:detail", kwargs={"pk": pk}))
    else:
        try:
            movie = movie_models.Movie.objects.get(pk=pk)
            return redirect(reverse("movies:detail", kwargs={"pk": pk}))
        except ObjectDoesNotExist:
            book = book_models.Book.objects.get(pk=pk)

            return redirect(reverse("books:detail", kwargs={"pk": pk}))


def delete_review(request, pk):

    user = request.user
    review = review_models.Review.objects.get(pk=pk)
    review_user = review.created_by
    if user == review_user:
        review.delete()
        return redirect(reverse("core:home"))
    else:
        return redirect(reverse("core:home"))
