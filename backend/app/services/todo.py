from fastapi import HTTPException
from app.models.todo import Todo
from app.schemas.todo import (
    TodoInputSchema,
    TodoOutputSchema,
    ListTodoSchema,
    UpdateTodoSchema,
)
from beanie import PydanticObjectId


async def create_todo(data: TodoInputSchema) -> TodoOutputSchema:
    todo = Todo(**data.dict())
    await todo.insert()
    return TodoOutputSchema(**todo.dict())


async def get_all_todos() -> ListTodoSchema:
    todos = await Todo.find_all().to_list()
    return {"todos": todos}


async def get_todo_by_id(todo_id: PydanticObjectId) -> TodoOutputSchema:
    todo = await Todo.get(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return TodoOutputSchema(**todo.dict())


async def delete_todo_by_id(todo_id: PydanticObjectId) -> None:
    todo = await Todo.get(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    await todo.delete()


async def update_todo_by_id(
    todo_id: PydanticObjectId, data: UpdateTodoSchema
) -> TodoOutputSchema:
    todo = await Todo.get(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.title = data.title
    todo.description = data.description
    todo.due_date = data.due_date
    todo.completed = data.completed
    await todo.save()
    return TodoOutputSchema(**todo.dict())
