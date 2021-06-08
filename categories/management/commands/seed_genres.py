from django.core.management.base import BaseCommand
from categories.models import Genre


class Command(BaseCommand):

    help = "Seed for Genres"

    def handle(self, *args, **options):
        genres = [
            "Action",
            "Comedy",
            "Drama",
            "Fantasy",
            "Horror",
            "Mystery",
            "Romance",
            "Thriller",
            "Documentary",
        ]

        for g in genres:
            Genre.objects.create(name=g)
        self.stdout.write(self.style.SUCCESS(f"{len(genres)} genres created!"))
