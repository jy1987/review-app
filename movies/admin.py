from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "year",
        "get_cover",
        "movie_genre",
        "rating",
        "director",
        "movie_cast",
        "total_rating",
    )

    list_filter = (
        "rating",
        "director",
        "cast",
    )

    def movie_genre(self, obj):  # 1 함수 이름과 list 이름이 같아야함. obj 는 row를 말하며, 여기선 Room 이다.
        genres = []
        for genre in obj.genre.all():  # Room에서 __str__ 로 name을 리턴했으므로 Room.name이 출력됨.
            genres.append(genre)

        return genres

    def movie_cast(self, obj):  # 1 함수 이름과 list 이름이 같아야함. obj 는 row를 말하며, 여기선 Room 이다.
        casts = []
        for cast in obj.cast.all():  # Room에서 __str__ 로 name을 리턴했으므로 Room.name이 출력됨.
            casts.append(cast)

        return casts

    def get_cover(self, obj):
        return mark_safe(f"<img width='35px' src={obj.cover_image.url} />")
