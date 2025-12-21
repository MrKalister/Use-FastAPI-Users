from fastapi import APIRouter

from api.api_v1.fastapi_users_router import fastapi_users_router
from api.dependencies.auth.backend import authentication_backend
from core.schemas.user import UserRead, UserCreate

router = APIRouter()

# The auth router will generate /login and /logout routes
# for a given authentication backend.
router.include_router(
    fastapi_users_router.get_auth_router(
        authentication_backend,
    ),
)

# The register router will generate a /register route
# to allow a user to create a new account.
router.include_router(
    fastapi_users_router.get_register_router(
        UserRead,
        UserCreate,
    ),
)

# Provides /request-verify-token and /verify routes
# to manage user e-mail verification.
# /request-verify-token - get token to verify
router.include_router(
    fastapi_users_router.get_verify_router(UserRead),
)

# Provides /forgot-password and /reset-password routes
# to allow a user to reset its password.
router.include_router(
    fastapi_users_router.get_reset_password_router(),
)
