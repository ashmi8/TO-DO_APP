from fastapi import APIRouter, Depends
from app.routes.user import router as user_router
from app.routes.auth import router as auth_router
from app.routes.todo import router as todo_router
from app.dependencies.auth import get_current_user


router = APIRouter(prefix="/api")

router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(
    todo_router,
    prefix="/todos",
    tags=["todos"],
    dependencies=[Depends(get_current_user)],
)
