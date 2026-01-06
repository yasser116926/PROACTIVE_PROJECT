from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    SYSTEM_ROLE_CHOICES = [
        ("admin", "Admin"),
        ("management", "Management"),
        ("user", "User"),
    ]

    system_role = models.CharField(
        max_length=20,
        choices=SYSTEM_ROLE_CHOICES,
        default="user"
    )

    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Profile(models.Model):

    PROFESSION_CHOICES = [
        ("management", "Management"),
        ("staff", "Staff"),
        ("instructor", "Instructor"),
        ("student", "Student Pilot"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    profession = models.CharField(
        max_length=30,
        choices=PROFESSION_CHOICES,
        blank=True
    )

    specialization = models.CharField(
        max_length=30,
        blank=True
    )

    student_number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        unique=True
    )

    nationality = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} Profile"
