from fastapi import FastAPI
from app.core.database import init_db


app = FastAPI(
    title="To-Do Application",
    description="A to-do application to manage their tasks efficiently.",
    version="1.0.0",
)

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the To-Do Application API"}

