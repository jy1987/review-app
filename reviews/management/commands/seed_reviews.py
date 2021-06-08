from django.core.management.base import BaseCommand
from django_seed import Seed
from movies.models import Movie
from books.models import Book
from users.models import User
from reviews.models import Review
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

        all_users = User.objects.all()
        all_movies = Movie.objects.all()
        all_books = Book.objects.all()
        seeder.add_entity(
            Review,
            int(total),
            {
                "rating": lambda x: random.randint(1, 5),
                "created_by": lambda x: random.choice(all_users),
                "movie": lambda x: random.choice(all_movies),
                "book": lambda x: random.choice(all_books),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{total} reviews created!"))
