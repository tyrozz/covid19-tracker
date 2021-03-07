from rest_framework import serializers

from covidtracker.tracker.models import Case, Location, TimeLine


class TimeLineSerializer(serializers.ModelSerializer):
    # location = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = TimeLine
        fields = "__all__"


class CaseSerializer(serializers.ModelSerializer):
    # location = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Case
        exclude = [
            "id",
        ]


class LocationSerializer(serializers.ModelSerializer):
    cases = CaseSerializer(many=True)
    timelines = TimeLineSerializer(many=True)

    class Meta:
        model = Location
        fields = "__all__"
