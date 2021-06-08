from enum import unique
import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from favs.models import FavList
from users.models import User
from movies.models import Movie
from books.models import Book
from faker import Faker


class Command(BaseCommand):

    help = "Seed for FavList"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=1,
            help="How many favs do you want?",
        )

    def handle(self, *args, **options):
        total = options.get("total")
        seeder = Seed.seeder()
        all_users = User.objects.all()
        all_movies = Movie.objects.all()
        all_books = Book.objects.all()
        seeder.add_entity(
            FavList,
            int(total),
        )
        """         created_lists = (
            seeder.execute()
        )  # room_models.Room 에 default 값만큼 배정 => dict 형태를 가짐
        print(created_lists)  # {<class 'rooms.models.Room'>: [43, 44]}
        print((created_lists.values()))  # dict_values([[43,44]])
        created_clean = flatten(
            list(created_lists.values())
        )  # flatten return list which is single level """
        for user in all_users:
            # print(user)
            get_number = random.randint(0, 3)
            if get_number % 2 == 0:
                lists = FavList.objects.create(created_by=user)

                for m in all_movies:
                    get_number = random.randint(0, 3)
                    if get_number % 3 == 0:
                        lists.movies.add(m)

                for b in all_books:
                    get_number = random.randint(0, 3)
                    if get_number % 3 == 0:
                        lists.books.add(b)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{total} favs created!"))
