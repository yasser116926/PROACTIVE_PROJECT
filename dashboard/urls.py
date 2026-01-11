from django.urls import path
from . import views
from gallery.views import GalleryUploadView
from flights.views import dashboard_flights
from .views import dashboard_view

app_name= "dashboard"

urlpatterns = [
    path('', views.dashboard_home, name='home'),
    path('post-news/', views.post_news_view, name='post-news'),
    path('create-class/', views.create_class, name='create-class'),
    path('create-event/', views.create_event, name='create-event'),
    path('upload-library-resource/', views.upload_library_resource, name='upload-library-resource'),
    path("gallery/", views.dashboard_gallery, name="dashboard-gallery"),
    path("gallery/upload/", GalleryUploadView.as_view(), name="dashboard-gallery-upload"),
    path("posts/add/", views.post_create_view, name="dashboard-post-add"),
    path("flights/", dashboard_flights, name="dashboard-flights"),
    path('vcr/',views.instructor_vcr_view, name='instructor-vcr'),



    path("dashboard/flights/", views.dashboard_flights, name="dashboard-flights"),
    path("dashboard/flights/delete/<int:flight_id>/", views.delete_flight, name="delete-flight"),
    path("dashboard/flights/clear/", views.clear_flights, name="clear-flights"),




]


   

