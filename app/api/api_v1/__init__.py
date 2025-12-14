from fastapi import APIRouter

from core.config import settings
from .auth import router as auth_router
from .users import router as users_router

router = APIRouter(prefix=settings.api.version)
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
