from fastapi import APIRouter,status
from app.schemas.user import UserInputSchema, UserOutputSchema, UserUpdateSchema,ListUsersSchema
from app.services.user import create_user, get_all_users_data, get_user_by_id, delete_user_by_id, update_user_by_id
from beanie import PydanticObjectId

router = APIRouter()

@router.post("/", response_model=UserOutputSchema,status_code=status.HTTP_201_CREATED)
async def add_user(user: UserInputSchema):
    created_user = await create_user(user)
    return created_user

@router.get("/",response_model=ListUsersSchema,status_code=status.HTTP_200_OK)
async def get_all_users():
    users = await get_all_users_data()
    return users

@router.get("/{user_id}", response_model=UserOutputSchema, status_code=status.HTTP_200_OK)
async def get_user(User_id: PydanticObjectId):
    user = await get_user_by_id(User_id)
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: PydanticObjectId):
    await delete_user_by_id(user_id)

@router.put("/{user_id}", response_model=UserOutputSchema, status_code=status.HTTP_200_OK)
async def update_user(user_id: PydanticObjectId, user: UserUpdateSchema):
    updated_user = await update_user_by_id(user_id, user)
    return updated_user




