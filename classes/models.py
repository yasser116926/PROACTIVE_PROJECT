from django.db import models
from accounts.models import User


class SchoolClass(models.Model):

    SUBJECT_CHOICES = [
        ("POF", "Principles of Flying"),
        ("MET", "Meteorology"),
        ("FPP", "Flight Planning & Performance"),
        ("AGK", "Aircraft General Knowledge"),
        ("NAV", "Navigation"),
        ("HPL", "Human Performance"),
        ("LAW", "Air Law"),
        ("RTC", "Radio & Communication"),
    ]

    CLASS_TYPE_CHOICES = [
        ("PPL", "PPL"),
        ("CPL", "CPL"),
        ("ATPL", "ATPL"),
    ]

    subject = models.CharField(
        max_length=50,
        choices=SUBJECT_CHOICES
    )

    instructor = models.CharField(max_length=100)

    class_room = models.CharField(
        max_length=10,
        choices=CLASS_TYPE_CHOICES
    )

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.get_subject_display()} | {self.class_room} | {self.date}"

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValueError("End time must be after start time")
