from django.urls import path
from . import views

urlpatterns = [
    # ✅ API MUST COME FIRST
    path('api/resources/', views.library_resources_api, name='library-resources-api'),

    path('', views.ResourceListView.as_view(), name='library-list'),
    path('upload/', views.LibraryResourceUploadView.as_view(), name='upload-library-resource'),
    path('my-resources/', views.MyLibraryResourcesView.as_view(), name='my-library-resources'),

    # ⚠️ dynamic paths ALWAYS go last
    path('<int:pk>/', views.ResourceDetailView.as_view(), name='library-detail'),
    path('<int:pk>/download/', views.library_resource_download, name='library-resource-download'),
    path('<int:pk>/edit/', views.edit_library_resource, name='edit-library-resource'),
    path('<int:pk>/delete/', views.LibraryResourceDeleteView.as_view(), name='delete-library-resource'),

    path('search/', views.search_library_resources, name='search-library-resources'),
    path('paginated/', views.paginated_library_list, name='paginated-library-list'),
]
