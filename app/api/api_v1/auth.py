from fastapi import APIRouter

from api.api_v1.fastapi_users_router import fastapi_users_router
from api.dependencies.auth.backend import authentication_backend

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)
router.include_router(
    fastapi_users_router.get_auth_router(authentication_backend),
)
