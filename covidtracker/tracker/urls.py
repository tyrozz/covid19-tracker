from django.urls import path

from covidtracker.tracker.views import CaseUploadDataView

app_name = "tracker"

urlpatterns = [
    path("caseupload/", CaseUploadDataView.as_view(), name="case-upload"),
]
