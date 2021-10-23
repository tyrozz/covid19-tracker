import csv
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.text import slugify

from ...models import Location


class Command(BaseCommand):
    help = "Load location data from CSV"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        start_time = timezone.now()
        file_path = options["file_path"]
        print(file_path)
        with open(file_path, "r") as csv_file:
            data = csv.reader(csv_file, delimiter=",")
            next(data, None)  #  this is to exclude header
            locations = []
            for row in data:
                location = Location(
                    location_code=row[0],
                    country_code=row[1],
                    iso2=row[2],
                    iso3=row[3],
                    fibs=row[4],
                    province_state=row[5],
                    country_region=row[6],
                    location_name=row[7],
                    slug=row[8],
                    country_population=row[9],
                    latitude=row[10],
                    longitute=row[11],
                )
                locations.append(location)
                if len(locations) > 5000:
                    Location.objects.bulk_create(locations)
                    locations = []
            if locations:
                Location.objects.bulk_create(locations)
        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )
