from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsAdminOrReadOnly


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    # Only admins can create, update, delete; others can read only

from django.shortcuts import render, redirect
from .forms import EventForm
from django.contrib.auth.decorators import user_passes_test
def is_staff_user(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_staff_user)
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard-home")
    else:
        form = EventForm()

    return render(request, "events/create_event.html", {"form": form})
