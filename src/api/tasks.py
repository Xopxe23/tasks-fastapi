import asyncio
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache

from src.api.dependencies import current_active_verified_user, get_task_service
from src.schemas.tasks import (TaskCreate, TaskRead, TasksCreateResponse,
                               TaskUpdate)
from src.schemas.users import UserRead
from src.services.tasks import TaskService
from src.utils.exceptions import NotFoundException

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("")
@cache(expire=60)
async def get_tasks(
    task_service: Annotated[TaskService, Depends(get_task_service)],
    user: UserRead = Depends(current_active_verified_user)
) -> list[TaskRead]:
    user_id = user.id
    tasks = await task_service.get_tasks(user_id=user_id)
    await asyncio.sleep(3)
    return tasks


@router.get("/{task_id}")
async def get_task_by_id(
    task_id: int,
    task_service: Annotated[TaskService, Depends(get_task_service)],
    user: UserRead = Depends(current_active_verified_user)
) -> TaskRead:
    task = await task_service.get_task_by_id(id=task_id, user_id=user.id)
    if not task:
        raise NotFoundException
    return task


@router.post("")
async def add_task(
    task: TaskCreate,
    task_service: Annotated[TaskService, Depends(get_task_service)],
    user: UserRead = Depends(current_active_verified_user)
) -> TasksCreateResponse:
    user_id = user.id
    task_id = await task_service.add_task(task=task, user_id=user_id)
    return TasksCreateResponse(task_id=task_id)


@router.put("/{task_id}")
async def update_task(
    task_id: int,
    task: TaskUpdate,
    task_service: Annotated[TaskService, Depends(get_task_service)],
    user: UserRead = Depends(current_active_verified_user)
) -> TaskRead:
    user_id = user.id
    task = await task_service.edit_task(id=task_id, user_id=user_id, task=task)
    if not task:
        raise NotFoundException
    return task


@router.delete("/{task_id}")
async def delete_task(
    task_id: int,
    task_service: Annotated[TaskService, Depends(get_task_service)],
    user: UserRead = Depends(current_active_verified_user)
) -> str:
    task_id = await task_service.delete_task(id=task_id, user_id=user.id)
    if not task_id:
        raise NotFoundException
    return f"Task with id: {task_id} deleted"
