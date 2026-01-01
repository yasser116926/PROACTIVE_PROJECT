from rest_framework import serializers
from .models import Aircraft, ScheduledFlight

class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ['id', 'name', 'registration_number']

class ScheduledFlightSerializer(serializers.ModelSerializer):
    aircraft = AircraftSerializer()
    instructor = serializers.StringRelatedField()
    student = serializers.StringRelatedField()

    class Meta:
        model = ScheduledFlight
        fields = ['id', 'flight_number', 'aircraft', 'instructor', 'student', 'date', 'time', 'status']
    def create(self, validated_data):
        aircraft_data = validated_data.pop('aircraft')
        aircraft, created = Aircraft.objects.get_or_create(**aircraft_data)
        scheduled_flight = ScheduledFlight.objects.create(aircraft=aircraft, **validated_data)
        return scheduled_flight