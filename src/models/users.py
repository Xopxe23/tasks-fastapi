from fastapi import Depends
from fastapi_users_db_sqlalchemy import (SQLAlchemyBaseUserTable,
                                         SQLAlchemyUserDatabase)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base, get_async_session


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(primary_key=True)


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
