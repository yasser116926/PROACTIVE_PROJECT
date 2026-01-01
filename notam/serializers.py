from rest_framework import serializers
from .models import Notam

class NotamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notam
        fields = "__all__"
        # Alternatively, specify fields explicitly:
        # fields = ['id', 'title', 'description', 'issued_at', 'valid_from', 'valid_to']