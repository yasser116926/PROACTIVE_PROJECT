from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, approve_users, signup_view, login_view
from . import views
from .views import profile_view
from .views import logout_view

from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
from .views import suspend_user, delete_user 


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
    path("suspend/<int:user_id>/", suspend_user, name="suspend"),
    path("delete/<int:user_id>/", delete_user, name="delete"),


    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/reset_password.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_done.html'), name='password_reset_complete'),
]









    
    



    
