from decimal import Decimal
from typing import TYPE_CHECKING, List

from .schema_base import SchemaBaseModel

if TYPE_CHECKING:
    from .review import ReviewResponse


class ProductRead(SchemaBaseModel):
    id: int
    name: str
    description: str
    price: Decimal
    stock_quantity: int
    category_id: int
    image_url: str | None = None


class ProductDetail(ProductRead):
    reviews: List[ReviewResponse] = []


class ProductUpdate(SchemaBaseModel):
    id: int
    name: str | None = None
    description: str | None = None
    price: Decimal | None = None
    stock_quantity: int | None = None
    category_id: int | None = None
