"""
Legacy aggregate for application models.

This module now proxies to the new `chefbot.infrastructure.persistence.db.models` (SQLAlchemy) and
`chefbot.interfaces.http.models` (Pydantic) packages. Prefer importing from those packages
directly to make intent explicit.
"""
from warnings import warn

from chefbot.interfaces.http.models.chat import ChatRequest, ChatResponse
from chefbot.interfaces.http.models.chat_message import (
    ChatMessageBase,
    ChatMessageCreate,
    ChatMessageResponse,
    ChatMessageUpdate,
    ChatSessionSnapshotBase,
    ChatSessionSnapshotCreate,
    ChatSessionSnapshotResponse,
)
from chefbot.interfaces.http.models.chat_session import ChatSessionCreate, ChatSessionResponse, ChatSessionUpdate
from chefbot.infrastructure.persistence.db.models import (
    ChatMessage,
    ChatSession,
    ChatSessionSnapshot,
    Conversation,
    ConversationHistorySnapshot,
    DialogueType,
    Message,
    User,
)

warn(
    "Importing from `chefbot.models` is deprecated. "
    "Use `chefbot.infrastructure.persistence.db.models` for database entities and "
    "`chefbot.interfaces.http.models` for Pydantic schemas instead.",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = [
    # Pydantic schemas (legacy re-export)
    "ChatRequest",
    "ChatResponse",
    "ChatMessageBase",
    "ChatMessageCreate",
    "ChatMessageUpdate",
    "ChatMessageResponse",
    "ChatSessionSnapshotBase",
    "ChatSessionSnapshotCreate",
    "ChatSessionSnapshotResponse",
    "ChatSessionCreate",
    "ChatSessionUpdate",
    "ChatSessionResponse",
    # SQLAlchemy models
    "ChatMessage",
    "ChatSession",
    "ChatSessionSnapshot",
    "Conversation",
    "ConversationHistorySnapshot",
    "DialogueType",
    "Message",
    "User",
]
