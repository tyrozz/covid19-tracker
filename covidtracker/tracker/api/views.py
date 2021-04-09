from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from covidtracker.tracker.models import Case, Location, TimeLine

from .serializers import CaseSerializer, LocationSerializer, TimeLineSerializer


class LocationViewSet(GenericViewSet, ListModelMixin):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
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


class TimeLineViewSet(GenericViewSet, ListModelMixin):
    serializer_class = TimeLineSerializer
    queryset = TimeLine.objects.all()
    filterset_fields = ("location",)


class CaseViewSet(GenericViewSet, ListModelMixin):
    serializer_class = CaseSerializer
    queryset = Case.objects.all()
    filterset_fields = (
        "location",
        "date",
    )
