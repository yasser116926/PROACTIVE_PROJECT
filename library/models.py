from django.conf import settings
from django.db import models


class LibraryResource(models.Model):

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

    subject = models.CharField(
        max_length=50,
        choices=SUBJECT_CHOICES
    )

    book_pdf = models.FileField(
        upload_to="library/books/",
        blank=True,
        null=True
    )

    question_bank_pdf = models.FileField(
        upload_to="library/question_banks/",
        blank=True,
        null=True
    )

    formulas_text = models.TextField(
        blank=True,
        null=True
    )

    diagrams_images = models.ImageField(
        upload_to="library/diagrams/",
        blank=True,
        null=True
    )

    external_links = models.TextField(
        blank=True,
        null=True,
        help_text="One link per line"
    )

    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.get_subject_display()
