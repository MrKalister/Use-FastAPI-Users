from fastapi import APIRouter

from core.config import settings
from .auth import router as auth_router

router = APIRouter(prefix=settings.api.version)
router.include_router(
    router=auth_router,
    prefix=settings.api.auth,
    tags=["Auth"],
)
