from django.contrib import admin

from covidtracker.tracker.models import Case, Location, TimeLine

admin.site.register(TimeLine)
admin.site.register(Location)
admin.site.register(Case)
