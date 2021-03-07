from django.db import models
from django.db.models import JSONField


class Location(models.Model):
    country_id = models.PositiveIntegerField()
    slug = models.SlugField(max_length=255, unique=True)
    country_code = models.CharField(max_length=50)
    country = models.CharField(max_length=255)
    country_population = models.PositiveIntegerField()
    province = models.CharField(max_length=255, blank=True, null=True)
    county = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.country


class Coordinates(models.Model):
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitute = models.DecimalField(max_digits=22, decimal_places=16)

    def __str__(self):
        return f"{self.location} {self.latitude} {self.longitute}"


class TimeLine(models.Model):
    location = models.ForeignKey(
        Location, related_name="timelines", on_delete=models.CASCADE
    )
    confirmed = JSONField(default=dict, blank=True, null=True)
    deaths = JSONField(default=dict, blank=True, null=True)
    recovered = JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return self.location.slug


class Case(models.Model):
    location = models.ForeignKey(
        Location, related_name="cases", on_delete=models.CASCADE
    )
    date = models.DateField(auto_now=False, auto_now_add=False)
    confirmed = models.PositiveIntegerField()
    deaths = models.PositiveIntegerField()
    recovered = models.PositiveIntegerField()

    def __str__(self):
        return self.location.country
