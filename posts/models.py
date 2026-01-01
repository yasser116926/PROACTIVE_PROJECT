from django.db import models
from accounts.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    published_date = models.DateField(auto_now_add=True)
    attachment = models.FileField(upload_to='posts/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
