from django.views.generic.edit import FormView

from covidtracker.tracker.forms import CaseDataForm
from covidtracker.tracker.models import Case


class CaseUploadDataView(FormView):
    login_url = "/api-auth/login/"
    template_name = "tracker/case_upload.html"
    form_class = CaseDataForm
    success_url = "/"

    def form_valid(self, form):
        form.bulk_create(Case)
        return super().form_valid(form)
