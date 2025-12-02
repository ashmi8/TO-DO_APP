from beanie import Document
from datetime import datetime, timezone


class BaseDocument(Document):
    created_at: datetime = datetime.now(timezone.utc)
    updated_at: datetime = datetime.now(timezone.utc)
