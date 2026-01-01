from rest_framework import serializers
from .models import Applicant

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['id', 'full_name', 'email', 'phone', 'applied_date', 'desired_course', 'status']
    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("Invalid email address.")
        return value