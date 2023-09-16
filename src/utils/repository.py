from abc import ABC, abstractmethod

from sqlalchemy import delete, insert, select, update

from src.db.db import async_session_maker


class AbstractRepository(ABC):

    @abstractmethod
    def find_all(self) -> list:
        pass

    @abstractmethod
    def find_by_id(self, id: int):
        pass

    @abstractmethod
    def add_one(self, data: dict) -> int:
        pass

    @abstractmethod
    def edit_one(self, id: int, data: dict) -> int:
        pass

    @abstractmethod
    def delete_one(self, id: int) -> int:
        pass


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def find_all(self, **filter_by) -> list:
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(**filter_by)
            result = await session.execute(stmt)
            result = [row[0].to_read_model() for row in result.all()]
            return result

    async def find_by_id(self, id: int, **filter_by):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(id=id, **filter_by)
            result = await session.execute(stmt)
            return result.scalar_one_or_none()

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one()

    async def edit_one(self, id: int, data: dict, **filter_by) -> int:
        async with async_session_maker() as session:
            stmt = update(self.model).values(**data).filter_by(id=id, **filter_by).returning(self.model)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one_or_none()

    async def delete_one(self, id: int, **filter_by) -> int:
        async with async_session_maker() as session:
            stmt = delete(self.model).filter_by(id=id, **filter_by).returning(self.model.id)
            task_id = await session.execute(stmt)
            await session.commit()
            return task_id
