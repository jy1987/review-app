from django.core.management.base import BaseCommand

from django_seed import Seed
from books.models import Book
from categories.models import Genre
from people.models import Person
import random


class Command(BaseCommand):

    help = "Seed for Books"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=1,
            help="How many books do you want?",
        )

    def handle(self, *args, **options):
        total = options.get("total")
        seeder = Seed.seeder()
        genre = Genre.objects.all()
        writer = Person.objects.all()

        print(Person.objects.all())
        seeder.add_entity(
            Book,
            int(total),
            {
                "rating": lambda x: random.randint(1, 5),
                "genre": lambda x: random.choice(genre),
                "writer": lambda x: random.choice(writer),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{total} movies created!"))
