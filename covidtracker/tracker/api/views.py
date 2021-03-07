from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from covidtracker.tracker.models import Case, Location, TimeLine

from .serializers import CaseSerializer, LocationSerializer, TimeLineSerializer


class LocationViewSet(GenericViewSet, ListModelMixin):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    filterset_fields = (
        "country_id",
        "slug",
        "country_code",
        "country",
        "province",
        "county",
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
