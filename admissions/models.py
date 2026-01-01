from django.db import models

class Applicant(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    applied_date = models.DateField(auto_now_add=True)
    desired_course = models.CharField(max_length=100)
    status_choices = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )
    status = models.CharField(max_length=10, choices=status_choices, default='pending')

    def __str__(self):
        return f"{self.full_name} ({self.status})"
class AdmissionInterview(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    interviewer = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Interview for {self.applicant.full_name} on {self.date}"