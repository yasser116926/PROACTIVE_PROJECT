from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, FlightAccess

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'is_approved', 'is_staff')
    list_filter = ('role', 'is_approved', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

@admin.register(FlightAccess)
class FlightAccessAdmin(admin.ModelAdmin):
    list_display = ("student", "approved", "approved_by", "approved_at")
    list_filter = ("approved",)
    search_fields = ("student__username", "student__email")
