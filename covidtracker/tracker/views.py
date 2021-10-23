import csv

from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView

from covidtracker.tracker.forms import CaseDataForm, LocationDataForm
from covidtracker.tracker.models import Case, Location

from .utils import staff_member_required


class CaseUploadDataView(FormView):
    login_url = "/api-auth/login/"
    template_name = "tracker/case_upload.html"
    form_class = CaseDataForm
    success_url = "/"

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.bulk_create_case(Case)
        return super().form_valid(form)


class LocationUploadDataView(FormView):
    login_url = "/api-auth/login/"
    template_name = "tracker/location_upload.html"
    form_class = LocationDataForm
    success_url = "/"

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.bulk_create_location(Location)
        return super().form_valid(form)


@staff_member_required
def download_locations_view(request):
    locations = Location.objects.all()
    response = HttpResponse(content_type="text/csv")
    response[
        "Content-Disposition"
    ] = 'attachment; filename="location-list-with-slug.csv"'
    writer = csv.writer(response)
    writer.writerow(
        [
            "location_code",
            "country_code",
            "iso2",
            "iso3",
            "fibs",
            "province_state",
            "country_region",
            "location_name",
            "slug",
            "country_population",
            "latitude",
            "longitute",
        ]
    )

    for location in locations:
        row = [
            location.location_code,
            location.country_code,
            location.iso2,
            location.iso3,
            location.fibs,
            location.province_state,
            location.country_region,
            location.location_name,
            location.slug,
            location.country_population,
            location.latitude,
            location.longitute,
        ]

        writer.writerow(row)
    return response