from . import BaseDocument
from pydantic import Field
from datetime import datetime


class Todo(BaseDocument):
    title: str
    description: str
    completed: bool = False
    due_date: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "todos"
