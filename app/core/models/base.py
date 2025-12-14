from sqlalchemy import MetaData
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declared_attr,
    mapped_column,
)

from core.config import settings
from utils import StrHelper


class Base(DeclarativeBase):
    __abstract__ = True
    # Use gives constraint_name.
    # It helps to delete a constraint in 'downgrade' of alembic.
    metadata = MetaData(naming_convention=settings.db.convention)

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{StrHelper.camel_to_snake_case(cls.__name__)}s"
