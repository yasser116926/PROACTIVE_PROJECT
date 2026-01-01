from rest_framework import serializers
from .models import SchoolClass
from django.utils import timezone

class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = ['subject', 'instructor', 'class_room', 'date', 'start_time', 'end_time']

    def validate_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Class date cannot be in the past.")
        return value

    def validate(self, data):
        # Ensure start_time < end_time
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        if start_time and end_time and start_time >= end_time:
            raise serializers.ValidationError("End time must be after start time.")
        return data
