from celery import Celery

celery = Celery(
    "tasks",
    broker="redis://localhost:6379",
    include=["src.tasks.tasks"]
)
