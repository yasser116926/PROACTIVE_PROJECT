from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('news/', views.news_page, name='news'),
    path('classes/', views.classes_page, name='classes'),
    path('events/', views.events_page, name='events'),
    path('gallery/', views.gallery_page, name='gallery'),
    path('library/', views.library_page, name='library'),
    path('posts/', views.posts_page, name='posts'),
    path('flight/', views.flight_page, name='flight'),
    path('notam/', views.notam_page, name='notam'),
    path('school/', views.school_page, name='school'),
    path('admission/', views.admission_page, name='admission'),
]
