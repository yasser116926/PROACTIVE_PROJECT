from rest_framework import serializers
from .models import Term, Content, Message, Connection

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = "__all__"

class TermSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    connections = ConnectionSerializer(many=True, read_only=True)

    class Meta:
        model = Term
        fields = "__all__"
        # Alternatively, specify fields explicitly:
        # fields = ['id', 'title', 'start_time', 'end_time', 'contents', 'messages', 'connections']