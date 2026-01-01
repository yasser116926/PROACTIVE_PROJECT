from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

def dashboard(request):
    return render(request, 'index.html')

def news_page(request):
    return render(request, 'news.html')

def classes_page(request):
    return render(request, 'classes.html')

def events_page(request):
    return render(request, 'events.html')

def gallery_page(request):
    return render(request, 'gallery.html')

def library_page(request):
    return render(request, 'library.html')

def posts_page(request):
    return render(request, 'posts.html')

def flight_page(request):
    return render(request, 'flight.html')

def notam_page(request):
    return render(request, 'notam.html')

def school_page(request):
    return render(request, 'school.html')

class PhotoList(APIView):   # ✅ must be a class
    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)   

def admission_page(request):
    return render(request, 'admission.html')
from django.http import JsonResponse