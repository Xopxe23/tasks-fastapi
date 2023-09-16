from src.api.users import fastapi_users
from src.repositories.tasks import TaskRepository
from src.services.tasks import TaskService


def get_task_service() -> TaskService:
    return TaskService(TaskRepository)


current_active_verified_user = fastapi_users.current_user(active=True, verified=True)
