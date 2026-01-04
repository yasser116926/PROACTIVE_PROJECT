from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, approve_users, signup_view, login_view, FlightApprovalList, ApproveFlight
from . import views
from .views import profile_view
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

app_name = "accounts"

urlpatterns = [
    path('', include(router.urls)),
    path("approve/", approve_users, name="approve"),
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("flight-approvals/", FlightApprovalList.as_view(), name="flight_approvals"),
    path("flight-approve/<int:student_id>/", ApproveFlight.as_view(), name="flight_approve"),
    path("pending/", views.pending_approval, name="pending"),
    path('profile/', profile_view, name='profile'),

]
