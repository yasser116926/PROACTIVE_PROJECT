"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from core import views  

from core.views import PhotoList 

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/', include('accounts.urls')),
    path('api/', include('flights.urls')), 
    path('api/', include('notam.urls')),
    path('api/', include('news.urls')),
    path('api/', include('classes.urls')),
    path('api/', include('events.urls')),
    path('api/', include('school.urls')),
    path('api/', include('admissions.urls')),
    path('api/', include('gallery.urls')),
    path('api/', include('posts.urls')),
    path('api/', include('library.urls')),
    path('api/', include('core.urls')),
    path('api/', include('dashboard.urls')),

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/photos/', PhotoList.as_view(), name='photo-list'),

    # Frontend pages
    path('', TemplateView.as_view(template_name="index.html")),
    path('news/', TemplateView.as_view(template_name="news.html")),
    path('flight/', TemplateView.as_view(template_name="flight.html")),
    path('notam/', TemplateView.as_view(template_name="notam.html")),
    path('school/', TemplateView.as_view(template_name="school.html")),
    path('admission/', TemplateView.as_view(template_name="admission.html")),
    path('classes/', TemplateView.as_view(template_name="classes.html")),
    path('events/', TemplateView.as_view(template_name="events.html")),
    path('gallery/', TemplateView.as_view(template_name="gallery.html")),
    path('posts/', TemplateView.as_view(template_name="posts.html")),
    path('library/', TemplateView.as_view(template_name="library.html")),
    path('photos/', views.PhotoList.as_view(), name='photo-list'),

    path('dashboard/', include('dashboard.urls')),
    path('news/', include('news.urls')),
    path("classes/", include("classes.urls")),
    path("events/", include("events.urls")),
    path("library/", include("library.urls")),
    path("gallery/", include("gallery.urls")),
    path("posts/", include("posts.urls")),
    path("flights/", include("flights.urls")),
    path("notam/", include("notam.urls")),
    path("school/", include("school.urls")),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),



    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='reset_password.html'), name='reset_password'),
    path('reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name='reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset_confirm.html'), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_done.html'), name='password_reset_complete'),

    







]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)