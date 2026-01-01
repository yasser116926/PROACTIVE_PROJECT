from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet
from . import views

router = DefaultRouter()
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.create_news, name='news-create'),
    path('', views.news_list, name='news-list'),
    
]
