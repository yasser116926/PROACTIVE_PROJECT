from django.shortcuts import render, redirect
from .forms import ClassForm
from rest_framework import viewsets
from .models import SchoolClass
from .serializers import SchoolClassSerializer  # create serializer if not already
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# DRF ViewSet
class SchoolClassViewSet(viewsets.ModelViewSet):
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Admin form view
def class_form_view(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class-form')  # reload form after saving
    else:
        form = ClassForm()
    return render(request, 'admin/classes_form.html', {'form': form})

from django.contrib.auth.decorators import user_passes_test

def is_staff_user(user):
    return user.is_authenticated and user.is_staff


def create_class(request):
    if not is_staff_user(request.user):
        return redirect('dashboard-login')  # redirect to login if not staff

    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard-home")
    else:
        form = ClassForm()
    return render(request, "classes/create_class.html", {"form": form})

def class_list(request):
    classes = SchoolClass.objects.all().order_by('name')
    return render(request, 'classes/class_list.html', {'classes': classes}) 
    
       