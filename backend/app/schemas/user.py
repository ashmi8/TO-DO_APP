from pydantic import BaseModel, EmailStr, Field
from beanie import Indexed, PydanticObjectId

class UserInputSchema(BaseModel):
    email: Indexed(EmailStr)
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    password: str = Field(..., min_length=8, max_length=128)

class UserOutputSchema(BaseModel):
    id: PydanticObjectId
    email: str
    first_name: str
    last_name: str
    password: str

