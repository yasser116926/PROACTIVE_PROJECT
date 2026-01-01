from django.db import models

class Flight(models.Model):
    AIRCRAFT_CHOICES = [
        ("5Y-CCZ", "5Y-CCZ"),
        ("5Y-PZO", "5Y-PZO"),
        ("FMX", "FMX"),
    ]

    aircraft = models.CharField(max_length=10, choices=AIRCRAFT_CHOICES)
    time = models.TimeField()
    name = models.CharField(max_length=100)
    ex = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["time"]

    def __str__(self):
        return f"{self.aircraft} - {self.time}"
