from api.users import fastapi_users
from repositories.tasks import TaskRepository
from services.tasks import TaskService


def get_task_service() -> TaskService:
    return TaskService(TaskRepository)


current_user = fastapi_users.current_user()
