from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    list_display = (
        "username",
        "language",
        "bio",
        "preference",
        "fav_books_genre",
        "fav_movies_genre",
    )

    list_filter = (
        "language",
        "preference",
        "favorite_book_genre",
        "favorite_movie_genre",
        "language",
        "superhost",
    )

    fieldsets = (
        (
            "custom profile",
            {
                "fields": (
                    "bio",
                    "preference",
                    "language",
                    "favorite_book_genre",
                    "favorite_movie_genre",
                    "superhost",
                )
            },
        ),
    ) + UserAdmin.fieldsets

    def fav_books_genre(
        self, obj
    ):  # 1 함수 이름과 list 이름이 같아야함. obj 는 row를 말하며, 여기선 Room 이다.
        all_books = []
        for (
            genre
        ) in (
            obj.favorite_book_genre.all()
        ):  # Room에서 __str__ 로 name을 리턴했으므로 Room.name이 출력됨.
            all_books.append(genre)

        return all_books

    def fav_movies_genre(
        self, obj
    ):  # 1 함수 이름과 list 이름이 같아야함. obj 는 row를 말하며, 여기선 Room 이다.
        all_movies = []
        for (
            genre
        ) in (
            obj.favorite_movie_genre.all()
        ):  # Room에서 __str__ 로 name을 리턴했으므로 Room.name이 출력됨.
            all_movies.append(genre)

        return all_movies
