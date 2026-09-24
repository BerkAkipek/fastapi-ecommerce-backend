from app.models.notification import NotificationType
from .schema_base import SchemaBaseModel


class NotificationRead(SchemaBaseModel):
    id: int
    recipient_email: str
    title: str
    message: str
    notification_type: NotificationType
