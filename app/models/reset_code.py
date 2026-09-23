from datetime import UTC, datetime, timedelta

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class ResetCode(Base):
    __tablename__ = "reset_codes"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, index=True)
    code: Mapped[str] = mapped_column(String, index=True, unique=True)
    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC) + timedelta(hours=2)
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), datetime.now(UTC)
    )
