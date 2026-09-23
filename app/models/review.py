from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from .product import Product
    from .user import User


class Review(Base):
    __tablename__ = "reviews"
    __table_args__ = CheckConstraint(
        "rating >= 1 AND rating <= 5", name="check_rating_range"
    )
    id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[int] = mapped_column(default=5)
    comment: Mapped[str] = mapped_column(String)
    username: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )
    # Foreign Key
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    uder_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    # Relations
    product: Mapped[Product] = relationship(back_populates="reviews")
    user: Mapped[User] = relationship(back_populates="reviews")
