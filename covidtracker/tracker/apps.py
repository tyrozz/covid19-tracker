from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TrackerConfig(AppConfig):
    name = "covidtracker.tracker"
    verbose_name = _("Tracker")
