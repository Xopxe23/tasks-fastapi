import uvicorn
from fastapi import FastAPI

from api.routers import routers

app = FastAPI(
    title="Tasks App"
)

for router in routers:
    app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
