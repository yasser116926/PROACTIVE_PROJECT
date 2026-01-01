from rest_framework import viewsets
from .models import Applicant
from .serializers import ApplicantSerializer
from rest_framework.permissions import IsAuthenticated

class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    permission_classes = [IsAuthenticated]  # only admins can see/manage
