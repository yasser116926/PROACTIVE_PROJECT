from django.db import models
from django.utils import timezone

CONTENT_TYPE_CHOICES = (
    ('text', 'Text'),
    ('pdf', 'PDF'),
    ('image', 'Image'),
    ('video', 'Video'),
)

class Term(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class Content(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='contents')
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES)
    data = models.TextField(help_text="For text, put text; for others, URL or path")
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='messages')
    user = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Connection(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='connections')
    user = models.CharField(max_length=100)
    is_instructor = models.BooleanField(default=False)
    connected_at = models.DateTimeField(auto_now_add=True)
    disconnected_at = models.DateTimeField(null=True, blank=True)

from django.db import models
from django.utils import timezone

class ClassSession(models.Model):
    title = models.CharField(max_length=200, default="Proactive VCR")
    is_live = models.BooleanField(default=False)
    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    def start(self):
        self.is_live = True
        self.started_at = timezone.now()
        self.save()

    def end(self):
        self.is_live = False
        self.ended_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.title} ({'LIVE' if self.is_live else 'OFF'})"
