from __future__ import annotations

from rest_framework import serializers
from .models import CustomUser, Message, Conversation


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model.

    Converts CustomUser instances to JSON and validates input.
    """

    class Meta:
        model: type[CustomUser] = CustomUser
        fields: str = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for the Message model.

    Includes sender details via nested UserSerializer.
    """

    sender: UserSerializer = UserSerializer(read_only=True)

    class Meta:
        model: type[Message] = Message
        fields: str = [
            "message_id",
            "sender",
            "message_body",
            "sent_at",
        ]


class ConversationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Conversation model.

    Includes participants and messages in a conversation.
    """

    participants: UserSerializer = UserSerializer(many=True, read_only=True)
    messages: MessageSerializer = MessageSerializer(many=True, read_only=True)

    class Meta:
        model: type[Conversation] = Conversation
        fields: str = [
            "conversation_id",
            "participants",
            "messages",
            "created_at",
        ]
