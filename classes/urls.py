from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SchoolClassViewSet, create_class
from . import views

router = DefaultRouter()
router.register(r'classes', SchoolClassViewSet, basename='classes')

urlpatterns = [
    path('', include(router.urls)),
    path('create-class/', views.create_class, name='create-class'),
]
