from django.db import models
from django.conf import settings


class GalleryImage(models.Model):
    image = models.ImageField(upload_to="gallery/images/")
    description = models.TextField(blank=True)
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"


class GalleryLike(models.Model):
    image = models.ForeignKey(
        GalleryImage,
        on_delete=models.CASCADE,
        related_name="likes"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("image", "user")

    def __str__(self):
        return f"{self.user} likes Image {self.image.id}"


class GalleryComment(models.Model):
    image = models.ForeignKey(
        GalleryImage,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user}"
