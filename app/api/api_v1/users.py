from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db_helper import db_helper
from core.schemas.user import UserIn, UserOut

from .crud import users as users_crud

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("", response_model=list[UserOut])
async def get_users(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    users = await users_crud.get_all_users(session=session)
    return users


@router.post("", response_model=UserOut)
async def create_user(
    user_in: UserIn,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    user = await users_crud.create_user(user_in=user_in, session=session)
    return user
