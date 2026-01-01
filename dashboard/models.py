from django.db import models
from accounts.models import User

class DashboardPost(models.Model):
    POST_TYPE_CHOICES = [
        ('news', 'News'),
        ('notam', 'NOTAM'),
        ('flight', 'Flight'),
        ('class', 'Class'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    post_type = models.CharField(max_length=20, choices=POST_TYPE_CHOICES)

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': True}
    )

    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.post_type})"
