from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from .forms import SignupForm
from django.utils import timezone

# Utility
def is_admin_or_management(user):
    if not user.is_authenticated:
        return False

    # Superusers always allowed
    if user.is_superuser:
        return True

    # Allowed admin, management roles
    if user.system_role in ["admin", "management"]:
        return user.is_approved

    return False




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
        target.system_role = role
        target.save()

        messages.success(request, f"{target.username} approved as {role}")
        return redirect("accounts:approve")

    return render(
        request,
        "accounts/approve_accounts.html",
        {"pending_users": pending_users}
    )

   
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

@login_required
def pending_approval(request):
    return render(request, "accounts/pending.html")


# accounts/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile.html', {
        'profile': profile,
        'form': form,
    })

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect("accounts:login")  

       