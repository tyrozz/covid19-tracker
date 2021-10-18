import random
from django.db import models
from django.db.models import JSONField
from django.utils.text import slugify


class Location(models.Model):
    location_code = models.IntegerField(
        help_text="Unique code for each location. For example Brussels-Belgium:5602, East Flanders-Belgium:5603",
        blank=True,
        null=True
    )
    country_code = models.IntegerField(
        help_text="Unique code for a country. For example Belgium:56",
        blank=True,
        null=True
    )
    iso2 = models.CharField(max_length=10, blank=True)
    iso3 = models.CharField(max_length=10, blank=True)
    fibs = models.CharField(max_length=10, blank=True)
    province_state = models.CharField(max_length=255, blank=True)
    country_region = models.CharField(max_length=255, blank=True)
    location_name = models.CharField(
        max_length=255, blank=True, help_text="For example Antwerp, Belgium"
    )
    slug = models.SlugField(max_length=255, unique=True)
    country_population = models.IntegerField(blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=11, decimal_places=8, blank=True, null=True
    )
    longitute = models.DecimalField(
        max_digits=11, decimal_places=8, blank=True, null=True
    )

    class Meta:
        ordering = [
            "id",
        ]

    def __str__(self):
        return self.location_name

    def save(self, *args, **kwargs):
        if not self.slug:
            value = self.location_code
            self.slug = slugify(value, allow_unicode=False)
            super().save(*args, **kwargs)


class TimeLine(models.Model):
    location = models.ForeignKey(
        Location, related_name="timelines", on_delete=models.CASCADE
    )
    confirmed = JSONField(default=dict, blank=True, null=True)
    deaths = JSONField(default=dict, blank=True, null=True)
    recovered = JSONField(default=dict, blank=True, null=True)

    class Meta:
        ordering = [
            "id",
        ]

    def __str__(self):
        return self.location.location_name


class Case(models.Model):
    location = models.ForeignKey(
        Location, related_name="cases", on_delete=models.CASCADE
    )
    date = models.DateField(auto_now=False, auto_now_add=False)
    confirmed = models.PositiveIntegerField()
    deaths = models.PositiveIntegerField()
    recovered = models.PositiveIntegerField()

    class Meta:
        ordering = ["-date", "id"]

    def __str__(self):
        return f"Cases in {self.location.location_name} in {self.date}"


# https://github.com/owid/covid-19-data/tree/master/public/data/vaccinations
class Vaccination(models.Model):
    location = models.ForeignKey(
        Location, related_name="vaccination", on_delete=models.CASCADE
    )
    date = models.DateField(auto_now=False, auto_now_add=False)
    vaccines = models.CharField(max_length=256, blank=True)
    total_vaccinations = models.PositiveIntegerField(
        blank=True, null=True, help_text="Total number of doses administered"
    )
    total_vaccinations_per_hundred = models.DecimalField(
        max_digits=2,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="total_vaccinations per 100 people",
    )
    people_vaccinated = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="total number of people who received at least one vaccine dose",
    )
    people_vaccinated_per_hundred = models.DecimalField(
        max_digits=2,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="people_vaccinated per 100 people",
    )
    people_fully_vaccinated = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="total number of people who received all doses prescribed",
    )
    people_fully_vaccinated_per_hundred = models.DecimalField(
        max_digits=2,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="people_fully_vaccinated per 100 people",
    )
    daily_vaccinations_raw = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="daily change in the total number of doses administered",
    )
    daily_vaccinations = models.PositiveIntegerField(
        blank=True, null=True, help_text="new doses administered per day"
    )
    daily_vaccinations_per_million = models.DecimalField(
        max_digits=2,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="daily_vaccinations per 1,000,000 people in the total population of the country.",
    )

    class Meta:
        ordering = ["-date", "id"]

    def __str__(self):
        return f"{self.people_vaccinated} people vaccinated in {self.location.location_name} as of {self.date}"


class Vaccine(models.Model):
    location = models.ForeignKey(
        Location, related_name="vaccines", on_delete=models.CASCADE
    )
    vaccines = models.CharField(max_length=256, blank=True, help_text="Vaccines")
    last_observation_date = models.DateField(auto_now=False, auto_now_add=False)
    source_name = models.CharField(max_length=256, blank=True)
    source_website = models.URLField(blank=True)

    class Meta:
        ordering = [
            "id",
        ]

    def __str__(self):
        return f"{self.vaccines} vaccine(s) used in {self.location} as of {self.last_observation_date}"
