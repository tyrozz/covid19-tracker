from django.contrib import admin

from covidtracker.tracker.models import Case, Location, TimeLine, Vaccination, Vaccine

admin.site.register(TimeLine)
admin.site.register(Location)
admin.site.register(Case)
admin.site.register(Vaccination)
admin.site.register(Vaccine)
