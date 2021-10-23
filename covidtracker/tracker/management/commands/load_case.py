import csv
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.text import slugify
from django.shortcuts import get_object_or_404

from ...models import Location, Case


class Command(BaseCommand):
    help = "Load Case data from CSV"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        start_time = timezone.now()
        file_path = options["file_path"]
        print(file_path)
        with open(file_path, "r") as csv_file:
            data = csv.reader(csv_file, delimiter=",")
            next(data, None)  #  this is to exclude header
            cases = []
            for row in data:
                slug = row[5]
                location = Location.objects.get(slug=slug)
                case = Case(
                    date=row[0],
                    confirmed=row[2],
                    recovered=row[3],
                    deaths=row[4],
                    location=location,
                )
                cases.append(case)
                if len(cases) > 5000:
                    Case.objects.bulk_create(cases)
                    cases = []
            if cases:
                Case.objects.bulk_create(cases)
        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )
