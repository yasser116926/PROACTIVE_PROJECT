from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import notam_channel, NotamViewSet

router = DefaultRouter()
router.register(r'notams', NotamViewSet)

urlpatterns = [
    # frontend NOTAM page
    path("", notam_channel, name="notam"),

]
