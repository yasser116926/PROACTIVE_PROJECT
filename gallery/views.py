from django.shortcuts import render, redirect
from django.views import View
from .forms import ImageForm
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from gallery.models import GalleryImage
from .serializers import GalleryImageSerializer
from .models import GalleryImage, GalleryLike, GalleryComment


# DRF ViewSet
class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]    
# Web Views 

class PhotoList(View):
    def get(self, request):
        photos = Photo.objects.all()
        return render(request, 'gallery/gallery.html', {'photos': photos})

class PhotoCreateView(View):
    def get(self, request):
        form = PhotoForm()
        return render(request, 'gallery/photo_form.html', {'form': form})

    def post(self, request):
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo-list')
        return render(request, 'gallery/photo_form.html', {'form': form})

from django.http import JsonResponse
from .models import GalleryImage

def gallery_api(request):
    images = GalleryImage.objects.all().order_by("-created_at")

    data = []
    for img in images:
        data.append({
            "id": img.id,
            "image": img.image.url,
            "description": img.description,
            "likes": img.likes.count(),
            "comments": img.comments.count(),
        })

    return JsonResponse(data, safe=False)
from rest_framework import viewsets

from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

def is_staff_user(user):
    return user.is_authenticated and user.is_staff

@method_decorator(user_passes_test(is_staff_user), name='dispatch')
class GalleryUploadView(View):
    def get(self, request):
        form = ImageForm()
        return render(request, "dashboard/upload_image.html", {"form": form})

    def post(self, request):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploaded_by = request.user
            photo.save()
            return redirect("dashboard-gallery")
        return render(request, "dashboard/upload_image.html", {"form": form})

from django.http import JsonResponse
from .models import GalleryImage

def gallery_images_api(request):
    images = GalleryImage.objects.all().order_by('-created_at')
    data = []

    for img in images:
        data.append({
            "id": img.id,
            "description": img.description,
            "image_url": img.image.url if img.image else None,
            "uploaded_by": img.uploaded_by.username if img.uploaded_by else None,
            "created_at": img.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "likes_count": img.likes.count(),
            "comments": [
                {
                    "user": comment.user.username,
                    "comment": comment.comment,
                    "created_at": comment.created_at.strftime("%Y-%m-%d %H:%M:%S")
                } 
                for comment in img.comments.all()
            ],
        })

    return JsonResponse(data, safe=False)

