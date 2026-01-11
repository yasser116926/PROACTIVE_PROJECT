from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from django.utils import timezone
from .forms import SignupForm, ProfileForm

from django import forms
from .models import Profile



# Utility
def is_admin_or_management(user):
    if not user.is_authenticated:
        return False

    # Superusers always allowed
    if user.is_superuser:
        return True

    # Allowed admin, management roles
    if user.system_role in ["admin", "management"]:
        return True

    return False




# Login view logic
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


# signup view logic

from .forms import SignupForm

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created. Awaiting approval.")
            return redirect("accounts:login")
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})




# =====================================================
# STUDENT NUMBER GENERATOR (UNIQUE)
# =====================================================

import random

def generate_student_number():
    while True:
        number = f"PR{random.randint(100000, 999999)}"
        if not Profile.objects.filter(student_number=number).exists():
            return number




# =====================================================
# APPROVAL DASHBOARD
# =====================================================

from .models import Profile, AccountApprovalLog

@login_required
@user_passes_test(is_admin_or_management)
def approve_users(request):
    pending_users = User.objects.filter(is_approved=False, is_superuser=False)

    if request.method == "POST":
        user_id = request.POST.get("user_id")
        profession = request.POST.get("profession")
        specialization = request.POST.get("specialization")

        user = get_object_or_404(User, id=user_id)

        # Approve user
        user.is_approved = True
        user.system_role = profession
        user.save()

        # Create / update profile
        profile, _ = Profile.objects.get_or_create(user=user)
        profile.specialization = specialization

        if profession.lower() == "student pilot":


            profile.student_number = generate_student_number()
        else:
            profile.student_number = None

        profile.save()

        # Log approval
        AccountApprovalLog.objects.update_or_create(
            user=user, defaults={"approved_at": timezone.now(), "approved_by": request.user}
        )

        messages.success(request, f"{user.username} approved successfully")
        return redirect("accounts:approve")

    return render(request, "accounts/approve_accounts.html", {"pending_users": pending_users})


#active accounts view logic


@login_required
@user_passes_test(is_admin_or_management)
def active_accounts(request):
    active_users = User.objects.filter(is_approved=True)
    return render(request, "accounts/active_accounts.html", {"active_users": active_users})

#suspend user logic

@login_required
@user_passes_test(is_admin_or_management)
def suspend_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.status = "suspended"
    user.save()
    return redirect("accounts:active_accounts")


#delete user logic

@login_required
@user_passes_test(is_admin_or_management)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect("accounts:active_accounts")




#user view logic   

from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  
    def get_queryset(self):
        if self.request.user.system_role in ["admin", "management"]:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save()   

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

#pending approval view logic

@login_required
def pending_approval(request):
    return render(request, "accounts/pending.html")


#profile view logic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User, Profile
from .forms import SignupForm, ProfileForm, EmailForm


@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    edit_mode = request.GET.get("edit") == "1"

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        email_form = EmailForm(request.POST, instance=request.user)

        if profile_form.is_valid() and email_form.is_valid():
            profile_form.save()
            email_form.save()
            return redirect("accounts:profile")

    else:
        profile_form = ProfileForm(instance=profile)
        email_form = EmailForm(instance=request.user)

    return render(request, "accounts/profile.html", {
        "profile": profile,
        "profile_form": profile_form,
        "email_form": email_form,
        "edit_mode": edit_mode,
    })





from django.contrib.auth import logout
from django.shortcuts import redirect

#logout view logic

def logout_view(request):
    logout(request)
    return redirect("accounts:login")  

       