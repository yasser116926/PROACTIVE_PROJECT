from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone


class User(AbstractUser):
    SYSTEM_ROLE_CHOICES = [
        ("admin", "Admin"),
        ("management", "Management"),
        ("staff", "Staff"),
        ("instructor", "Instructor"),
        ("student", "Student"),
    ]

    system_role = models.CharField(
        max_length=20,
        choices=SYSTEM_ROLE_CHOICES,
        default="student",
    )

    is_approved = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10,
        choices=[("active", "Active"), ("suspended", "Suspended")],
        default="active"
    )

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profiles/", blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    nationality = models.CharField(max_length=50, blank=True)
    specialization = models.CharField(max_length=50, blank=True)
    student_number = models.CharField(max_length=10, blank=True, null=True, unique=True)

    def __str__(self):
        return f"{self.user.username} Profile"


class AccountApprovalLog(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    approved_at = models.DateTimeField(default=timezone.now)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="approver"
    )

    def __str__(self):
        return f"{self.user.username} approved on {self.approved_at}"
