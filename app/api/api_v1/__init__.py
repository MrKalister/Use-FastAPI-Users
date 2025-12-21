from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from core.config import settings
from .auth import router as auth_router
from .messages import router as messages_router
from .users import router as users_router

http_bearer_auth = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix=settings.api.version,
    # add dependency to have an option
    # to authorize with a token
    dependencies=[Depends(http_bearer_auth)],
)

router.include_router(
    router=auth_router,
    prefix=settings.api.auth,
    tags=[settings.api.auth.removeprefix("/")],
)
router.include_router(
    router=users_router,
    prefix=settings.api.users,
    tags=[settings.api.users.removeprefix("/")],
)
router.include_router(
    router=messages_router,
    prefix=settings.api.messages,
    tags=[settings.api.messages.removeprefix("/")],
)
