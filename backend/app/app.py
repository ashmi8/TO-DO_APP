from fastapi import FastAPI
from app.core.database import init_db
from app.routes.router import router as api_router

app = FastAPI(
    title="To-Do Application",
    description="A to-do application to manage their tasks efficiently.",
    version="1.0.0",
)


@app.on_event("startup")
async def on_startup():
    await init_db()


app.include_router(api_router)
