from __future__ import annotations

from rest_framework import viewsets
from .models import CustomUser, Message, Conversation
from .serializers import UserSerializer, MessageSerializer, ConversationSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for handling User CRUD operations."""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """ViewSet for handling Message CRUD operations."""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    """ViewSet for handling Conversation CRUD operations."""
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
