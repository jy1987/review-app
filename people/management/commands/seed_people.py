from django.core.management.base import BaseCommand
from django_seed import Seed
from people.models import Person
import random


class Command(BaseCommand):

    help = "Seed for People"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=1,
            help="How many users do you want?",
        )

    def handle(self, *args, **options):
        total = options.get("total")
        seeder = Seed.seeder()
        seeder.add_entity(
            Person,
            int(total),
            {
                "name": lambda x: seeder.faker.name(),
                "photo": lambda x: f"people/{random.randint(1,6)}.jpeg",
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{total} people created!"))
