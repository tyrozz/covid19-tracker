from rest_framework import serializers

from covidtracker.tracker.models import Case, Location, TimeLine, Vaccination, Vaccine


class VaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccination
        exclude = ["id"]


class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        exclude = ["id"]


class TimeLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeLine
        exclude = [
            "id",
        ]


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        exclude = [
            "id",
        ]


class LocationSerializer(serializers.ModelSerializer):
    cases = CaseSerializer(many=True)
    timelines = TimeLineSerializer(many=True)
    vaccines = VaccineSerializer(many=True)
    vaccination = VaccinationSerializer(many=True)

    class Meta:
        model = Location
        fields = "__all__"
