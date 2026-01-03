from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from .models import User, FlightAccess
from .forms import SignupForm
from django.utils import timezone

# Utility
def is_admin_or_management(user):
    return user.role in ["admin", "management"]



# Login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return redirect("accounts:login")

    return render(request, "signup.html")



# Approve users (admin/management)
@login_required
@user_passes_test(is_admin_or_management)
def approve_users(request):
    pending_users = User.objects.filter(is_approved=False, is_superuser=False)

    if request.method == "POST":
        user_id = request.POST.get("user_id")
        role = request.POST.get("role")

        target = get_object_or_404(User, id=user_id)

        target.is_approved = True
        target.role = role
        target.save()

        messages.success(request, f"{target.username} approved as {role}")
        return redirect("accounts:approve")

    return render(
        request,
        "accounts/approve_accounts.html",
        {"pending_users": pending_users}
    )


# Flight approvals API
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class FlightApprovalList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role not in ["admin", "management", "instructor"]:
            return Response({"detail": "Not allowed"}, status=403)
        approvals = FlightAccess.objects.select_related("student")
        data = [{"student": fa.student.username, "approved": fa.approved} for fa in approvals]
        return Response(data)

class ApproveFlight(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, student_id):
        if request.user.role not in ["admin", "management", "instructor"]:
            return Response({"detail": "Not allowed"}, status=403)
        access = get_object_or_404(FlightAccess, student_id=student_id)
        access.approved = True
        access.approved_by = request.user
        access.approved_at = timezone.now()
        access.save()
        return Response({"status": "approved"})

from rest_framework import viewsets
from .serializers import UserSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  
    def get_queryset(self):
        if self.request.user.role in ["admin", "management"]:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save()   

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def pending_approval(request):
    return render(request, "accounts/pending.html")
       