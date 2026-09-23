from datetime import UTC, datetime
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from .cart import Cart
    from .order import Order


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    CUSTOMER = "CUSTOMER"
    DELIVERY = "DELIVERY"


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True, index=True)
    password: Mapped[str | None] = mapped_column(String, nullable=True, default=None)
    name: Mapped[str] = mapped_column(String, index=True)
    profile_picture: Mapped[str | None] = mapped_column(String, default=None)
    address: Mapped[str | None] = mapped_column(String, default=None)
    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole), default=UserRole.CUSTOMER, index=True
    )
    active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default = lambda: datetime.now(UTC)
    )
    # One To Many Relation
    orders: Mapped[list[Order]] = relationship(back_populates="users")
    reviews: Mapped[list[Order]] = relationship(back_populates="users") 
    # One To One Realtion
    cart: Mapped[Cart | None] = relationship(back_populates="users", uselist=False)
    