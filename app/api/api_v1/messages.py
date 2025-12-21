"""
That's just test router
to show how to get and use current_user_depends
"""

from fastapi import APIRouter, Depends

from api.api_v1.fastapi_users_router import (
    current_active_user,
    current_active_superuser_user,
)
from core.models import User
from core.schemas.user import UserRead

router = APIRouter()


@router.get("")
def get_user_messages(
    user: User = Depends(current_active_user),
):
    return {
        "messages": ["m1", "m2", "m3"],
        "user": UserRead.model_validate(user),
    }


@router.get("/secrets")
def get_super_user_messages(
    user: User = Depends(current_active_superuser_user),
):
    return {
        "messages": ["secret_m1", "secret_m2", "secret_m3"],
        "user": UserRead.model_validate(user),
    }
