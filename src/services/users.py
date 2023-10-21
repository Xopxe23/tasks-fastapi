from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin
from httpx_oauth.clients.discord import DiscordOAuth2

from src.config import settings
from src.models.users import User, get_user_db
from src.tasks.tasks import sent_verification_email

SECRET = settings.SECRET

discord_oauth_client = DiscordOAuth2("1165180777366040626", "cjp0fSOsLyat3vZXRKipZxMds4aDhCVS")


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User: {user.email} has registered with id: {user.id}.")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")
        sent_verification_email.delay(user.email, token)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
