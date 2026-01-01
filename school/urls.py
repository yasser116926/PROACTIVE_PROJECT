from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import TermViewSet, ContentViewSet, MessageViewSet, ConnectionViewSet

router = DefaultRouter()
router.register("terms", TermViewSet)
router.register("contents", ContentViewSet)
router.register("messages", MessageViewSet)
router.register("connections", ConnectionViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("dashboard/school/<int:class_id>/", views.instructor_school_view, name="dashboard-school"),
]
