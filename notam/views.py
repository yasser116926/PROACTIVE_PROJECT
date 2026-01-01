from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect

from .models import Notam
from .serializers import NotamSerializer
from .forms import NotamForm
from notam.services.notam_importer import refresh_if_needed
from django.utils import timezone


# API
from rest_framework.permissions import AllowAny

class NotamViewSet(viewsets.ModelViewSet):
    queryset = Notam.objects.all().order_by("-date", "-time")
    serializer_class = NotamSerializer
    permission_classes = [AllowAny]
# Admin Views




from django.utils import timezone

def notam_channel(request):
    refresh_if_needed()

    airports = ["HKJK", "HKNW", "HKMO"]
    grouped_notams = {}

    for airport in airports:
        grouped_notams[airport] = Notam.objects.filter(
            airport=airport,
            date_expiry__gte=timezone.now().date()
        ).order_by("-date", "-time")

    return render(request, "notam.html", {
        "grouped_notams": grouped_notams
    })



