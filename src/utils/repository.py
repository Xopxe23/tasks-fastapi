from abc import ABC, abstractmethod

from sqlalchemy import insert, select

from db.db import async_session_maker


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
            return result.scalar_one().to_read_model()

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one()
