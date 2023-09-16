from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db import Base
from src.schemas.tasks import TaskRead


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    def to_read_model(self) -> TaskRead:
        return TaskRead(
            id=self.id,
            user_id=self.user_id,
            title=self.title,
            description=self.description,
            created_at=self.created_at
        )
