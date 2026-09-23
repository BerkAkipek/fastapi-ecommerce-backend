from datetime import UTC, datetime
from decimal import Decimal
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Numeric, String
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from .order import Order


class PaymentStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"


class Payment(Base):
    __tablename__ = "payments"
    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[Decimal] = mapped_column(
        Numeric(precision=10, scale=2), default=Decimal("0.00")
    )
    currency: Mapped[str] = mapped_column(String, default="tr")
    status: Mapped[PaymentStatus] = mapped_column(
        SQLEnum(PaymentStatus), default=PaymentStatus.PENDING
    )
    # Stripe transaction id
    provider_transaction_id: Mapped[str] = mapped_column(
        String, index=True, unique=True
    )
    payment_method: Mapped[str] = mapped_column(String)
    # Foreign Key
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), unique=True)
    # One to One Relations
    order: Mapped[Order] = relationship(back_populates="payment")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )
