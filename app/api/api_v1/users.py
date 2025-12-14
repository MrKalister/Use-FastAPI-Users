from fastapi import APIRouter

from api.api_v1.fastapi_users_router import fastapi_users_router
from core.schemas.user import UserRead, UserUpdate

router = APIRouter()

# The auth router will generate /me and /{id} routes
# to get information about current user account.
router.include_router(
    fastapi_users_router.get_users_router(
        UserRead,
        UserUpdate,
    ),
)
