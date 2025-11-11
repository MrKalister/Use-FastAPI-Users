import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.config import settings

from api import router as api_router
from core.db_helper import db_helper


@asynccontextmanager
async def lifespan(this_app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


app = FastAPI(
    lifespan=lifespan,
)
app.include_router(
    router=api_router,
    prefix=settings.api.prefix,
)


if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
