from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from src.config import settings
from src.models.users import User
from src.schemas.users import UserCreate, UserRead
from src.services.users import discord_oauth_client, get_user_manager
from src.utils.auth import auth_backend

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

router.include_router(
    fastapi_users.get_oauth_router(
        discord_oauth_client,
        auth_backend,
        settings.SECRET,
        is_verified_by_default=True,
    ),
    prefix="/discord",
)

router.include_router(
    fastapi_users.get_oauth_associate_router(discord_oauth_client, UserRead, settings.SECRET),
    prefix="/associate/discord",
)
