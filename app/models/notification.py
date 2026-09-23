from datetime import UTC, datetime
from enum import Enum

from sqlalchemy import DateTime, String
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class NotificationType(str, Enum):
    WELCOME = "welcome"
    ORDER_UPDATE = "order_update"
    PAYMENT_UPDATE = "payment_update"
    PROMOTIONAL = "promotional"
    SECURITY = "security"


class Notification(Base):
    __tablename__ = "notifications"
    id: Mapped[int] = mapped_column(primary_key=True)
    recipient_email: Mapped[str] = mapped_column(String, index=True)
    title: Mapped[str] = mapped_column(String)
    message: Mapped[str] = mapped_column(String)
    notification_type: Mapped[NotificationType] = mapped_column(
        SQLEnum(NotificationType), default=NotificationType.ORDER_UPDATE
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )
