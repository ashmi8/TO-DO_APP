from pydantic import EmailStr, Field
from beanie import Indexed
from . import BaseDocument

class User(BaseDocument):
    email: Indexed(EmailStr, unique=True)
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    hashed_password: str
    is_active: bool | None = True

    class Settings:
        name = "users"


