import csv
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.text import slugify
from django.shortcuts import get_object_or_404

from ...models import Location, TimeLine


class Command(BaseCommand):
    help = "Load Timeline data from CSV"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        start_time = timezone.now()
        file_path = options["file_path"]
        print(file_path)
        with open(file_path, "r") as csv_file:
            data = csv.reader(csv_file, delimiter=",")
            next(data, None)  #  this is to exclude header
            timelines = []
            for row in data:
                slug = row[5]
                date = str(row[0])
                confirmed = row[2]
                recovered = row[3]
                deaths = row[4]

                location = Location.objects.get(slug=slug)
                timeline, created = TimeLine.objects.get_or_create(location=location)
                timeline.confirmed[date] = int(confirmed)
                timeline.recovered[date] = int(recovered)
                timeline.deaths[date] = int(deaths)

                timelines.append(timeline)
                if len(timelines) > 5000:
                    TimeLine.objects.bulk_update(
                        timelines, fields=["confirmed", "deaths", "recovered"]
                    )
                    timelines = []
            if timelines:
                TimeLine.objects.bulk_update(
                    timelines, fields=["confirmed", "deaths", "recovered"]
                )
        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )
