from fastapi import HTTPException
from app.schemas.user import UserInputSchema, UserOutputSchema
from app.models.user import User

async def create_user(user : UserInputSchema)-> UserOutputSchema:
    existing_user = await User.find_one(User.email == user.email)
    if  existing_user: 
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )
    new_user = await User.insert(User(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        hashed_password=user.password  # In a real application, hash the password here
    ))
    return UserOutputSchema(
        id=new_user.id,
        email=new_user.email,
        first_name=new_user.first_name,
        last_name=new_user.last_name,
        password=new_user.hashed_password
    )