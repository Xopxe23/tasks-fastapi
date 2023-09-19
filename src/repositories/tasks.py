from sqlalchemy import select

from src.db.db import async_session_maker
from src.models.tasks import Task
from src.utils.repository import SQLAlchemyRepository


class TaskRepository(SQLAlchemyRepository):
    model = Task
