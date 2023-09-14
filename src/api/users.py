from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from models.users import User
from schemas.users import UserCreate, UserRead
from services.users import get_user_manager
from utils.auth import auth_backend

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="",
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
)

router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="",
)
