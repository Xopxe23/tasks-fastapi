import uvicorn
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from src.config import settings

from src.api.routers import routers

app = FastAPI(
    title="Tasks App"
)

for router in routers:
    app.include_router(router)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}", encoding="utf-8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")


# if __name__ == "__main__":
#     uvicorn.run(app="main:app", reload=True)
