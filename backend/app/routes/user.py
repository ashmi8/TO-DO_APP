from fastapi import APIRouter,status
from app.schemas.user import UserInputSchema, UserOutputSchema
from app.services.usser import create_user

router = APIRouter()

@router.post("/", response_model=UserOutputSchema,status_code=status.HTTP_201_CREATED)
async def add_user(user: UserInputSchema):
    created_user = await create_user(user)
    return created_user

