from src.schemas.tasks import TaskCreate, TaskRead, TaskUpdate
from src.utils.repository import AbstractRepository


class TaskService:
    def __init__(self, tasks_repo: AbstractRepository) -> None:
        self.tasks_repo: AbstractRepository = tasks_repo()

    async def get_tasks(self, user_id: int) -> list[TaskRead]:
        tasks = await self.tasks_repo.find_all(user_id=user_id)
        return tasks

    async def get_task_by_id(self, id: int, user_id: int) -> TaskRead:
        task = await self.tasks_repo.find_by_id(id, user_id=user_id)
        return task

    async def add_task(self, task: TaskCreate, user_id: int) -> int:
        task_data = task.model_dump()
        task_data["user_id"] = user_id
        task_id = await self.tasks_repo.add_one(task_data)
        return task_id

    async def edit_task(self, id: int, user_id: int, task: TaskUpdate) -> TaskRead:
        task_data = task.model_dump()
        task = await self.tasks_repo.edit_one(id=id, data=task_data, user_id=user_id)
        return task

    async def delete_task(self, id: int, user_id: int) -> int:
        await self.tasks_repo.delete_one(id=id, user_id=user_id)
