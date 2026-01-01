from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("management", "Management"),
        ("instructor", "Instructor"),
        ("student", "Student"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="student")
    is_approved = models.BooleanField(default=False)
    can_access_flights = models.BooleanField(default=False)

    def __str__(self):
        return self.username


from django.conf import settings
from django.db import models

class FlightAccess(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_flights')
    approved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.username} - {'Approved' if self.approved else 'Pending'}"
    
class UserRole(models.Model):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("management", "Management"),
        ("instructor", "Instructor"),
        ("student", "Student"),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="student")

    def __str__(self):
        return f"{self.user.username} - {self.role}"    

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=UserRole.ROLE_CHOICES, default="student")
    approved = models.BooleanField(default=False)
    can_access_flights = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} Profile"


      