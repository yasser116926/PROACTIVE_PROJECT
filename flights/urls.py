from django.urls import path
from .views import dashboard_flights, flights_dashboard_api

urlpatterns = [
    path("dashboard/", dashboard_flights, name="dashboard-flights"),
    path("api/dashboard/", flights_dashboard_api, name="flights-dashboard-api"),
]
