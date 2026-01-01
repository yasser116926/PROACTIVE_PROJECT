from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Term, Content, Message, Connection, ClassSession
from .serializers import (
    TermSerializer,
    ContentSerializer,
    MessageSerializer,
    ConnectionSerializer
)
from django.shortcuts import render

# ----------------- DRF ViewSets -----------------

class TermViewSet(viewsets.ModelViewSet):
    # Term model uses 'start_time' and 'end_time'
    queryset = Term.objects.all().order_by("-start_time")
    serializer_class = TermSerializer
    permission_classes = [IsAuthenticated]

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated]

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    permission_classes = [IsAuthenticated]

# ----------------- Django Views -----------------

def school_channel(request):
    # ClassSession model uses 'started_at', 'ended_at'
    session = ClassSession.objects.filter(is_live=True).first()

    return render(request, "school.html", {
        "session": session
    })

def instructor_school_view(request, class_id):
    session = ClassSession.objects.filter(
        instructor=request.user,
        class_id=class_id,
        is_live=True
    ).first()

    context = {
        "class_id": class_id,
        "session": session
    }
    return render(request, "school/instructor_school.html", context)
