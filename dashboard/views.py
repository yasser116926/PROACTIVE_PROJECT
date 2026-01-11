from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from accounts.utils import can_access_dashboard
# =========================================================
# ACCESS CONTROL (SINGLE SOURCE OF TRUTH)
# =========================================================

def can_access_dashboard(user):
    if not user.is_authenticated:
        return False

    # Superusers always allowed
    if user.is_superuser:
        return True

    # Allowed staff roles
    if user.system_role in ["admin", "management", "staff", "instructor"]:
        return user.is_approved

    return False


@login_required
@user_passes_test(can_access_dashboard)
def dashboard_view(request):
    return render(request,"dashboard/home.html")

# =========================================================
# DASHBOARD HOME
# =========================================================

@login_required
@user_passes_test(can_access_dashboard)
def dashboard_home(request):
    return render(request, "dashboard/home.html")


# =========================================================
# NEWS
# =========================================================

from news.forms import NewsForm

@user_passes_test(can_access_dashboard)
def post_news_view(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard-home")
    else:
        form = NewsForm()

    return render(request, "dashboard/post_news.html", {"form": form})

# =========================================================
# CLASSES
# =========================================================

from classes.forms import ClassForm

@user_passes_test(can_access_dashboard)
def create_class(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard-home")
    else:
        form = ClassForm()

    return render(request, "dashboard/create_class.html", {"form": form})

# =========================================================
# EVENTS
# =========================================================

from events.forms import EventForm

@user_passes_test(can_access_dashboard)
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard-home")
    else:
        form = EventForm()

    return render(request, "dashboard/create_event.html", {"form": form})

# =========================================================
# LIBRARY
# =========================================================

from library.forms import LibraryResourceForm

@user_passes_test(can_access_dashboard)
def upload_library_resource(request):
    if request.method == "POST":
        form = LibraryResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboard-home")
    else:
        form = LibraryResourceForm()

    return render(request, "dashboard/upload_library.html", {"form": form})

# =========================================================
# GALLERY
# =========================================================

from gallery.models import GalleryImage

@user_passes_test(can_access_dashboard)
def dashboard_gallery(request):
    images = GalleryImage.objects.all().order_by("-created_at")
    return render(
        request,
        "dashboard/gallery.html",
        {"images": images}
    )

# =========================================================
# POSTS
# =========================================================

from posts.forms import PostForm

@user_passes_test(can_access_dashboard)
def post_create_view(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboard-home")
    else:
        form = PostForm()

    return render(request, "dashboard/posts_form.html", {"form": form})

# =========================================================
# FLIGHTS
# =========================================================

from flights.forms import FlightForm
from flights.models import Flight

@user_passes_test(can_access_dashboard)
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

# =========================================================
# INSTRUCTOR VCR
# =========================================================

from school.models import ClassSession

@user_passes_test(can_access_dashboard)
def instructor_vcr_view(request):
    session = ClassSession.objects.filter(is_live=True).first()
    return render(
        request,
        "dashboard/vcr.html",
        {"session": session}
    )




from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from flights.models import Flight   # adjust import if needed


def is_staff(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(is_staff)
def delete_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    flight.delete()
    return redirect("dashboard-flights")


@user_passes_test(is_staff)
def clear_flights(request):
    Flight.objects.all().delete()
    return redirect("dashboard-flights")



