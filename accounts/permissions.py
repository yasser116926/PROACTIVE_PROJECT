from accounts.models import User
from django.contrib.auth.models import AnonymousUser




def can_access_flights(user):
    if not user.is_authenticated:
        return False

    profile = user.profile

    if profile.role in ["ADMIN", "MANAGEMENT"]:
        return True

    if profile.role == "INSTRUCTOR" and profile.approved:
        return True

    if profile.role == "STUDENT" and profile.approved:
        return True

    return False


def can_access_notams(user):
    return can_access_flights(user)

from rest_framework.permissions import BasePermission
from .models import FlightAccess


class HasFlightAccess(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        # Full access roles
        if user.role in ["admin", "management", "instructor"]:
            return True

        # Students must be approved
        if user.role == "student":
            return FlightAccess.objects.filter(
                student=user,
                approved=True
            ).exists()

        return False
from rest_framework.exceptions import PermissionDenied
def check_flight_access(user):
    if user.role == "student":
        if not hasattr(user, "flight_access"):
            raise PermissionDenied("Flight access not approved")

        if not user.flight_access.approved:
            raise PermissionDenied("Flight access not approved")
    return True