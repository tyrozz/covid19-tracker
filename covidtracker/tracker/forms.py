import pandas as pd
from django import forms
from django.shortcuts import get_object_or_404

from covidtracker.tracker.bulk_create_manager import BulkCreateManager
from covidtracker.tracker.models import Location


class CaseDataForm(forms.Form):
    data_file = forms.FileField()

    def bulk_create(self, modelname):
        data_frame = pd.read_csv(self.cleaned_data["data_file"].file)

        bulk_mgr = BulkCreateManager(chunk_size=20)
        for index, row in data_frame.iterrows():
            location_name = location = row["location"]
            location = get_object_or_404(Location, country=location_name)
            bulk_mgr.add(
                modelname(
                    location=location,
                    date=row["date"],
                    confirmed=row["confirmed"],
                    deaths=row["deaths"],
                    recovered=row["recovered"],
                )
            )
        bulk_mgr.done()
