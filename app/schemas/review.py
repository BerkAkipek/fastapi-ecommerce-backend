from datetime import datetime

from pydantic import Field

from .schema_base import SchemaBaseModel


class ReviewCreate(SchemaBaseModel):
    order_id: int
    product_id: int
    rating: int = Field(ge=1, le=5, description="Ratings in between 1 and 5")


class ReviewResponse(SchemaBaseModel):
    id: int
    rating: int
    comment: str
    username: str
    created_at: datetime
    product_id: int
    user_id: int
