from fastapi import APIRouter, status
from app.schemas.todo import (
    TodoInputSchema,
    TodoOutputSchema,
    ListTodoSchema,
    UpdateTodoSchema,
)
from app.services.todo import (
    create_todo,
    get_all_todos,
    get_todo_by_id,
    delete_todo_by_id,
    update_todo_by_id,
)
from beanie import PydanticObjectId

router = APIRouter()


@router.post("/", response_model=TodoOutputSchema, status_code=status.HTTP_201_CREATED)
async def add_todo(todo: TodoInputSchema):
    new_todo = await create_todo(todo)
    return new_todo


@router.get("/", response_model=ListTodoSchema, status_code=status.HTTP_200_OK)
async def read_all_todos():
    todos = await get_all_todos()
    return todos


@router.get(
    "/{todo_id}", response_model=TodoOutputSchema, status_code=status.HTTP_200_OK
)
async def read_todo(todo_id: PydanticObjectId):
    todo = await get_todo_by_id(todo_id)
    return todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: PydanticObjectId):
    return await delete_todo_by_id(todo_id)


@router.put(
    "{todo_id}", response_model=TodoOutputSchema, status_code=status.HTTP_200_OK
)
async def update_todo(todo_id: PydanticObjectId, data: UpdateTodoSchema):
    todo = await update_todo_by_id(todo_id, data)
    return todo
