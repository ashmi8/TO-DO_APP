from beanie import init_beanie
from pymongo import AsyncMongoClient
from app.core.config import settings
from app.models.user import User

async def init_db():
    db_client = AsyncMongoClient(settings.DATABASE_URL)
    

    # Initialize beanie with the Product document class
    await init_beanie(database=db_client[settings.DATABASE_NAME], document_models=[
        User,
    ])
    
    print("Database initialized successfully.")


