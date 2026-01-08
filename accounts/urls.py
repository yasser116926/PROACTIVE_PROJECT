from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, approve_users, signup_view, login_view
from . import views
from .views import profile_view
from .views import logout_view

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

app_name = "accounts"

urlpatterns = [
    
    path('', include(router.urls)),
    path("approve/", approve_users, name="approve"),
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("pending/", views.pending_approval, name="pending"),
    path('profile/', profile_view, name='profile'),
    path("logout/", logout_view, name="logout"),
    path("active/", views.active_accounts, name="active_accounts"),
    path("active/suspend/<int:user_id>/", views.suspend_user, name="suspend_user"),
    path("active/delete/<int:user_id>/", views.delete_user, name="delete_user"),




]
