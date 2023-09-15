from sqlalchemy import select

from db.db import async_session_maker
from models.tasks import Task
from utils.repository import SQLAlchemyRepository


class TaskRepository(SQLAlchemyRepository):
    model = Task

    # async def find_all(self, user_id: int) -> list:
    #     async with async_session_maker() as session:
    #         stmt = select(self.model).where(user_id=user_id)
    #         result = await session.execute(stmt)
    #         result = [row[0].to_read_model for row in result.all()]
    #         return result

    # async def find_by_id(self, id: int, user_id: int) -> list:
    #     async with async_session_maker() as session:
    #         stmt = select(self.model).where(id=id, user_id=user_id)
    #         result = await session.execute(stmt)
    #         return result.scalar_one_or_none()
