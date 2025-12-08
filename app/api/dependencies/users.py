from typing import Annotated, TYPE_CHECKING

from fastapi import Depends

from core.db_helper import db_helper
from core.models import User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.session_getter),
    ],
):
    yield User.get_user_db(session)
