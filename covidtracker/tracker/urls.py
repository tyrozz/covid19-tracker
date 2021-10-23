from django.urls import path

from covidtracker.tracker.views import (
    CaseUploadDataView,
    LocationUploadDataView,
    download_locations_view,
)

app_name = "tracker"

urlpatterns = [
    path("case-upload/", CaseUploadDataView.as_view(), name="case-upload"),
    path("location-upload/", LocationUploadDataView.as_view(), name="location-upload"),
    path("download-locations/", download_locations_view, name="download-locations"),
]
