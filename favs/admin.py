from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.FavList)
class FavAdmin(admin.ModelAdmin):

    list_display = (
        "created_by",
        "set_books",
        "set_movies",
    )

    list_filter = ("created_by",)

    def set_books(self, obj):  # 1 함수 이름과 list 이름이 같아야함. obj 는 row를 말하며, 여기선 Room 이다.
        all_books = []
        for book in obj.books.all():  # Room에서 __str__ 로 name을 리턴했으므로 Room.name이 출력됨.
            all_books.append(book)

        return all_books

    set_books.short_description = "books"

    def set_movies(self, obj):  # 1 함수 이름과 list 이름이 같아야함. obj 는 row를 말하며, 여기선 Room 이다.
        all_movies = []
        for movie in obj.movies.all():  # Room에서 __str__ 로 name을 리턴했으므로 Room.name이 출력됨.
            all_movies.append(movie)

        return all_movies

    set_movies.short_description = "movies"
