from datetime import datetime
from typing import Optional

from pydantic import BaseModel, constr


class TaskRead(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    created_at: datetime

    class Config:
        from_attributes = True


class TaskCreate(BaseModel):
    title: constr(min_length=3, max_length=100)
    description: constr(max_length=250)


class TaskUpdate(BaseModel):
    title: Optional[constr(min_length=3, max_length=100)] = None
    description: Optional[constr(max_length=250)] = None


class TasksCreateResponse(BaseModel):
    task_id: int

    class Config:
        from_attributes = True
