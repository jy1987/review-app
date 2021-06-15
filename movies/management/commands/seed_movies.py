from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.admin.utils import flatten
from django_seed import Seed
from movies.models import Movie
from categories.models import Genre, Category
from people.models import Person
import random


class Command(BaseCommand):

    help = "Seed for Movies"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=1,
            help="How many movies do you want?",
        )

    def handle(self, *args, **options):
        total = options.get("total")
        seeder = Seed.seeder()
        favorite_movie_genre = Genre.objects.all()

        director = Person.objects.all()
        cast = Person.objects.all()
        print(cast)
        seeder.add_entity(
            Movie,
            int(total),
            {
                "title": lambda x: seeder.faker.word(),
                "rating": lambda x: random.randint(1, 5),
                "cover_image": lambda x: f"movie/{random.randint(1,8)}.jpeg",
                "director": lambda x: random.choice(director),
            },
        )

        created_movies = (
            seeder.execute()
        )  # room_models.Room 에 default 값만큼 배정 => dict 형태를 가짐
        print(created_movies)  # {<class 'rooms.models.Room'>: [43, 44]}
        print((created_movies.values()))  # dict_values([[43,44]])
        created_clean = flatten(
            list(created_movies.values())
        )  # flatten return list which is single level

        for pk in created_clean:

            movies = Movie.objects.get(pk=pk)

            for g in favorite_movie_genre:
                get_number = random.randint(0, 3)
                if get_number % 2 == 0:
                    movies.genre.add(g)

            for c in cast:
                get_number = random.randint(0, 3)
                if get_number % 2 == 0:
                    movies.cast.add(c)

        # genre = favorite_movie_genre[random.randint(1, 3) : random.randint(4, 7)]
        # cast = cast[random.randint(1, 5) : random.randint(20, 25)]
        # movies.genre.add(*genre)
        # movies.cast.add(*cast)
        # manytomany 만드는 방법

        self.stdout.write(self.style.SUCCESS(f"{total} movies created!"))
