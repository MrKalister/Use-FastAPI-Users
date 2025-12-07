from typing import TYPE_CHECKING

from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from .base import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, SQLAlchemyBaseUserTable[int]):
    @classmethod
    def get_user_db(cls, session: 'AsyncSession'):
        return SQLAlchemyUserDatabase(session, User)
