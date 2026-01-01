from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from functools import wraps

def access_required(channel):
    def decorator(view_func):
        @login_required
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            profile = request.user.profile

            if not profile.is_approved:
                return HttpResponseForbidden("Account not approved")

            if channel == "flights" and not profile.can_access_flights:
                return HttpResponseForbidden("Flights access denied")

            return view_func(request, *args, **kwargs)

        return _wrapped_view
    return decorator
def flights_access_required(view_func):
    return access_required("flights")(view_func)

from django.http import HttpResponseForbidden

def role_required(roles):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.role not in roles:
                return HttpResponseForbidden("Access denied")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
