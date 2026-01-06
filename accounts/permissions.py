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




