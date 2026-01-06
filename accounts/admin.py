from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "username",
        "email",
        "system_role",
        "is_active",
        "is_approved",
        "is_staff",
    )
    list_filter = (
        "system_role",
        "is_approved",
        "is_staff",
        "is_superuser",
        "is_active",
    )
    search_fields = ("username", "email")
    ordering = ("username",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "profession",
        "specialization",
        "student_number",
        "approved",
    )
    list_filter = ("profession", "approved")
