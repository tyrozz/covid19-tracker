from django.db import models
from django.db.models import JSONField
from django.utils.text import slugify


class Location(models.Model):
    location_code = models.PositiveIntegerField(
        help_text="Unique code for each location. For example Brussels-Belgium:5602, East Flanders-Belgium:5603"
    )
    country_code = models.PositiveIntegerField(
        help_text="Unique code for a country. For example Belgium:56"
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
    country_population = models.PositiveIntegerField(blank=True)
    latitude = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True
    )
    longitute = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True
    )

    def __str__(self):
        return self.location_name

    def save(self, *args, **kwargs):
        if not self.slug:
            value = self.location_name
            self.slug = slugify(value, allow_unicode=False)
            super().save(*args, **kwargs)


class TimeLine(models.Model):
    location = models.ForeignKey(
        Location, related_name="timelines", on_delete=models.CASCADE
    )
    confirmed = JSONField(default=dict, blank=True, null=True)
    deaths = JSONField(default=dict, blank=True, null=True)
    recovered = JSONField(default=dict, blank=True, null=True)

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

    def __str__(self):
        return self.location.location_name
