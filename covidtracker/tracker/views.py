from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView

from covidtracker.tracker.forms import CaseDataForm, LocationDataForm
from covidtracker.tracker.models import Case, Location


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
