from pydantic import BaseModel, Field
from datetime import datetime
from beanie import PydanticObjectId
from typing import Optional


class TodoInputSchema(BaseModel):
    title: str
    description: str | None = None
    due_date: datetime = Field(default_factory=datetime.utcnow)
    completed: bool = False


class TodoOutputSchema(BaseModel):
    id: PydanticObjectId
    title: str
    description: str | None = None
    due_date: datetime = Field(default_factory=datetime.utcnow)
    completed: bool = False


class ListTodoSchema(BaseModel):
    todos: list[TodoOutputSchema]


class UpdateTodoSchema(BaseModel):
    title: str | None = None
    description: str | None = None
    due_date: datetime = Field(default_factory=datetime.utcnow)
    completed: bool | None = None
