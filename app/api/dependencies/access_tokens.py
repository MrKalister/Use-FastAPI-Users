from typing import Annotated, TYPE_CHECKING

from fastapi import Depends

from core.db_helper import db_helper
from core.models import AccessToken

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_token_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.session_getter),
    ],
):
    yield AccessToken.get_access_token_db(session)
