from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies import current_user, get_task_service
from exceptions import NotFoundException
from schemas.tasks import TaskCreate, TaskRead, TasksCreateResponse, TaskUpdate
from schemas.users import UserRead
from services.tasks import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("")
async def get_tasks(
    task_service: Annotated[TaskService, Depends(get_task_service)],
    user: UserRead = Depends(current_user)
) -> list[TaskRead]:
    user_id = user.id
    tasks = await task_service.get_tasks(user_id=user_id)
    return tasks


@router.get("/{task_id}")
async def get_task_by_id(
    task_id: int,
    task_service: Annotated[TaskService, Depends(get_task_service)],
    user: UserRead = Depends(current_user)
) -> TaskRead:
    task = await task_service.get_task_by_id(id=task_id, user_id=user.id)
    if not task:
        raise NotFoundException
    return task


@router.post("")
async def add_task(
    task: TaskCreate,
    task_service: Annotated[TaskService, Depends(get_task_service)],
    user: UserRead = Depends(current_user)
) -> TasksCreateResponse:
    user_id = user.id
    task_id = await task_service.add_task(task=task, user_id=user_id)
    return TasksCreateResponse(task_id=task_id)


@router.put("/{task_id}")
async def update_task(
    task_id: int,
    task: TaskUpdate,
    task_service: Annotated[TaskService, Depends(get_task_service)],
    user: UserRead = Depends(current_user)
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
    user: UserRead = Depends(current_user)
) -> str:
    task_id = await task_service.delete_task(id=task_id, user_id=user.id)
    if not task_id:
        raise NotFoundException
    return f"Task with id: {task_id} deleted"
