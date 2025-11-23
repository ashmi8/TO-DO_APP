from fastapi import HTTPException
from app.schemas.user import UserInputSchema, UserOutputSchema
from app.models.user import User
from beanie import PydanticObjectId
from app.dependencies.auth import get_password_hash

async def create_user(user : UserInputSchema)-> UserOutputSchema:
    existing_user = await User.find_one(User.email == user.email)
    if  existing_user: 
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )
    hased_password = get_password_hash(user.password)
    new_user = await User.insert(User(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        hashed_password=hased_password  
    ))
    return UserOutputSchema(
        id=new_user.id,
        email=new_user.email,
        first_name=new_user.first_name,
        last_name=new_user.last_name,
        password=new_user.hashed_password
    )

async def get_all_users_data() -> list[UserOutputSchema]:
    users = await User.find_all().to_list()
    return [
        UserOutputSchema(
            id=user.id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            password=user.hashed_password
        ) for user in users
    ]

async def get_user_by_id(user_id: PydanticObjectId) -> UserOutputSchema:
    existing_user = await User.find_one(User.id == user_id)
    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return UserOutputSchema(
        id=existing_user.id,
        email=existing_user.email,
        first_name=existing_user.first_name,
        last_name=existing_user.last_name,
        password=existing_user.hashed_password)

async def delete_user_by_id(user_id : PydanticObjectId) -> None:
    existing_user = await User.find_one(User.id == user_id)
    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    await existing_user.delete()

async def update_user_by_id(user_id: PydanticObjectId, user_data: UserInputSchema) -> UserOutputSchema:
    existing_user = await User.find_one(User.id == user_id)
    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    existing_user.first_name = user_data.first_name
    existing_user.last_name = user_data.last_name
    existing_user.hashed_password = user_data.password  # In a real application, hash the password here
    await existing_user.save()
    return UserOutputSchema(
        id=existing_user.id,
        email=existing_user.email,
        first_name=existing_user.first_name,
        last_name=existing_user.last_name,
        password=existing_user.hashed_password)


    
