import pandas as pd
from django import forms
from django.shortcuts import get_object_or_404
from django.utils.text import slugify

from covidtracker.tracker.bulk_create_manager import BulkCreateManager
from covidtracker.tracker.models import Location


class CaseDataForm(forms.Form):
    data_file = forms.FileField()

    def bulk_create_case(self, modelname):
        data_frame = pd.read_csv(self.cleaned_data["data_file"].file)

        bulk_mgr = BulkCreateManager(chunk_size=20)
        for index, row in data_frame.iterrows():
            location_name = row["location"]
            location = get_object_or_404(Location, country_region=location_name)
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


class LocationDataForm(forms.Form):
    data_file = forms.FileField()

    def bulk_create_location(self, modelname):
        data_frame = pd.read_csv(self.cleaned_data["data_file"].file)

        bulk_mgr = BulkCreateManager(chunk_size=20)
        for index, row in data_frame.iterrows():
            value = row["location_name"]
            slug = slugify(value, allow_unicode=False)
            bulk_mgr.add(
                modelname(
                    location_code=row["location_code"],
                    country_code=row["country_code"],
                    iso2=row["iso2"],
                    iso3=row["iso3"],
                    fibs=row["fibs"],
                    province_state=row["province_state"],
                    country_region=row["country_region"],
                    location_name=row["location_name"],
                    country_population=row["country_population"],
                    latitude=row["latitude"],
                    longitute=row["longitute"],
                    slug=slug,
                )
            )
        bulk_mgr.done()
