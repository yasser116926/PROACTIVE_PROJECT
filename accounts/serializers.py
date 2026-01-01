from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

from .models import FlightAccess

class FlightAccessSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.get_full_name", read_only=True)

    class Meta:
        model = FlightAccess
        fields = [
            "id",
            "student",
            "student_name",
            "approved",
            "approved_by",
            "approved_at",
        ]
        read_only_fields = ("approved_by", "approved_at")
