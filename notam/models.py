from django.db import models
from django.utils import timezone
from datetime import time

PRIORITY_CHOICES = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
)

class Notam(models.Model):
    airport = models.CharField(
        max_length=4,
        help_text="ICAO code e.g. HKJK, HKNW, HKMO"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField(default=time(0, 0))
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='low'
    )
    date_issued = models.DateField(auto_now_add=True)
    date_expiry = models.DateField()

    def is_active(self):
        return self.date_expiry >= timezone.now().date()

    def __str__(self):
        return f"{self.airport} - {self.title}"
