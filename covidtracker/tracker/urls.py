from django.urls import path

from covidtracker.tracker.views import CaseUploadDataView, LocationUploadDataView

app_name = "tracker"

urlpatterns = [
    path("case-upload/", CaseUploadDataView.as_view(), name="case-upload"),
    path("location-upload/", LocationUploadDataView.as_view(), name="location-upload"),
]
