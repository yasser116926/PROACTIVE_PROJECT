from django.contrib import admin

# Register your models here.
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "is_active")
    list_filter = ("is_active", "published_date")
    search_fields = ("title", "content")
