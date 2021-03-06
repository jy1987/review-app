from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("kind",)

    list_filter = ("kind",)


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "movies_genre",
        "books_genre",
    )

    list_filter = ("name",)

    def movies_genre(self, obj):
        all_movies = []
        for genre in obj.movie.all():
            all_movies.append(genre)

        return all_movies

    def books_genre(self, obj):
        all_books = []
        for genre in obj.books.all():
            all_books.append(genre)

        return all_books
