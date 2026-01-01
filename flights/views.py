from django.http import JsonResponse
from .models import Flight
from .services.weather import get_metar, get_taf

def flights_dashboard_api(request):
    icao = request.GET.get("icao", "HKJK")

    flights = Flight.objects.all()

    data = {
        "weather": {
            "icao": icao,
            "metar": get_metar(icao),
            "taf": get_taf(icao),
        },
        "flights": {
            "5Y-CCZ": [],
            "5Y-PZO": [],
            "FMX": [],
        }
    }

    for flight in flights:
        data["flights"][flight.aircraft].append({
            "time": flight.time.strftime("%H:%M"),
            "name": flight.name,
            "ex": flight.ex,
        })

    return JsonResponse(data)

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .forms import FlightForm
from .models import Flight

def is_staff(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_staff)
def dashboard_flights(request):
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard-flights")
    else:
        form = FlightForm()

    flights = Flight.objects.all()

    return render(
        request,
        "dashboard/flights.html",
        {
            "form": form,
            "flights": flights,
        }
    )
   

# flights/views.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from accounts.permissions import can_access_flights

@login_required
def flights_view(request):
    profile = request.user.profile

    if not profile.is_approved or not profile.can_access_flights:
        return HttpResponseForbidden("Flights access not approved")

    return render(request, "flights/flights.html")

    if not can_access_flights(request.user):
        return HttpResponseForbidden("Approval required")

    return render(request, "flights/flights.html")

from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

def check_flight_access(user):
    if user.role == "student":
        if not hasattr(user, "flight_access"):
            raise PermissionDenied("Flight access not approved")

        if not user.flight_access.approved:
            raise PermissionDenied("Flight access not approved")
    return True

from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import FlightAccess
from accounts.permissions import HasFlightAccess
class FlightApprovalList(APIView):
    permission_classes = [IsAuthenticated, HasFlightAccess]

    def get(self, request):
        if request.user.profile.role not in ["ADMIN", "MANAGEMENT", "INSTRUCTOR"]:
            return HttpResponseForbidden()

        pending_requests = FlightAccess.objects.filter(approved=False)
        data = [
            {
                "student_id": fa.student.id,
                "student_username": fa.student.user.username,
                "requested_at": fa.requested_at,
            }
            for fa in pending_requests
        ]
        return Response(data)

@login_required
def flights_view(request):
    if request.user.role == "student":
        return redirect("/")
    return render(request, "flights.html")
