from rest_framework.viewsets import ReadOnlyModelViewSet

from covidtracker.tracker.models import Case, Location, TimeLine, Vaccination, Vaccine

from .serializers import (
    CaseSerializer,
    LocationSerializer,
    TimeLineSerializer,
    VaccinationSerializer,
    VaccineSerializer,
)


class LocationViewSet(ReadOnlyModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.prefetch_related(
        "timelines", "cases", "vaccination", "vaccines"
    ).all()
    filterset_fields = (
        "location_code",
        "country_code",
        "slug",
        "iso2",
        "iso3",
        "fibs",
        "province_state",
        "country_region",
        "location_name",
        "country_population",
        "latitude",
        "longitute",
    )


class TimeLineViewSet(ReadOnlyModelViewSet):
    serializer_class = TimeLineSerializer
    queryset = TimeLine.objects.select_related("location").all()
    filterset_fields = ("location",)


class CaseViewSet(ReadOnlyModelViewSet):
    serializer_class = CaseSerializer
    queryset = Case.objects.select_related("location").all()
    filterset_fields = (
        "location",
        "date",
    )


class VaccineViewSet(ReadOnlyModelViewSet):
    serializer_class = VaccineSerializer
    queryset = Vaccine.objects.select_related("location").all()
    filterset_fields = ("location",)


class VaccinationViewSet(ReadOnlyModelViewSet):
    serializer_class = VaccinationSerializer
    queryset = Vaccination.objects.select_related("location").all()
    filterset_fields = ("location",)
