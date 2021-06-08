from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users.models import User
from categories.models import Genre

import random


class Command(BaseCommand):

    help = "Seed for User"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=1,
            help="How many users do you want?",
        )

    def handle(self, *args, **options):
        total = options.get("total")
        seeder = Seed.seeder()
        favorite_movie_genre = Genre.objects.all()
        favorite_book_genre = Genre.objects.all()
        print(favorite_movie_genre)
        seeder.add_entity(
            User,
            int(total),
            {
                "superhost": False,
            },
        )

        created_favs = (
            seeder.execute()
        )  # room_models.Room 에 default 값만큼 배정 => dict 형태를 가짐
        print(created_favs)  # {<class 'rooms.models.Room'>: [43, 44]}
        print((created_favs.values()))  # dict_values([[43,44]])
        created_clean = flatten(
            list(created_favs.values())
        )  # flatten return list which is single level

        for pk in created_clean:

            user = User.objects.get(pk=pk)
            print(user)

            to_add_movie = favorite_movie_genre[
                random.randint(2, 4) : random.randint(5, 8)
            ]
            to_add_book = favorite_book_genre[
                random.randint(2, 4) : random.randint(5, 8)
            ]

            user.favorite_movie_genre.add(*to_add_movie)
            user.favorite_book_genre.add(*to_add_book)
            # manytomany 만드는 방법

        self.stdout.write(self.style.SUCCESS(f"{total} favs created!"))
