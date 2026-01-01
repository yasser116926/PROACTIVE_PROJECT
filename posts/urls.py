from django.urls import path
from .views import post_create_view
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('form/', post_create_view, name='post-form'),
    path("posts/add/", post_create_view, name="dashboard-post-add"),

]

urlpatterns += router.urls
