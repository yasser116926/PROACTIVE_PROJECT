from django.urls import path
from . import views

urlpatterns = [
    path("api/", views.gallery_api, name="gallery-api"),
    path("api/images/", views.gallery_images_api, name="gallery-images-api"),
    path("upload/", views.GalleryUploadView.as_view(), name="gallery-upload"),
]
