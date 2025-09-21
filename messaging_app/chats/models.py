from __future__ import annotations

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Custom user model extending Django's
    AbstractUser.

    Attributes
    ----------
    user_id : UUIDField
        Unique identifier for the user
        (primary key).
    email : EmailField
        Unique and required email address.
    phone_number : CharField
        Optional phone number of the user.
    role : CharField
        Role of the user, chosen from 'admin',
        'mod', or 'user'.
    created_at : DateTimeField
        Timestamp when the user was created.
    """

    class Role(models.TextChoices):
        """Enumeration of user roles."""
        ADMIN: str = "admin", "Administrator"
        MODERATOR: str = "mod", "Moderator"
        USER: str = "user", "Regular User"

    user_id: uuid.UUID = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True,
    )
    email: str = models.EmailField(
        unique=True,
        null=False,
        db_index=True
    )
    phone_number: str = models.CharField(
        max_length=20,
        blank=True
    )
    role: str = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER,
    )
    created_at: str = models.DateTimeField(
        auto_now_add=True
    )


class Message(models.Model):
    """
    Model representing a message sent by a user.

    Attributes
    ----------
    message_id : UUIDField
        Unique identifier for the message (primary key).
    sender : ForeignKey
        Reference to the user who sent the message.
    message_body : TextField
        Content of the message (required).
    sent_at : DateTimeField
        Timestamp when the message was sent.
    """

    message_id: uuid.UUID = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True,
    )
    sender: CustomUser = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="messages",
    )
    message_body: str = models.TextField(null=False)
    sent_at: str = models.DateTimeField(
        auto_now_add=True
    )


class Conversation(models.Model):
    """
    Model representing a conversation between users.

    Attributes
    ----------
    conversation_id : UUIDField
        Unique identifier for the conversation
        (primary key).
    participants : ForeignKey
        Reference to a user participating in the
        conversation.
    created_at : DateTimeField
        Timestamp when the conversation was created.
    """

    conversation_id: uuid.UUID = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True,
    )
    participants: CustomUser = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="conversations",
    )
    created_at: str = models.DateTimeField(
        auto_now_add=True
    )
