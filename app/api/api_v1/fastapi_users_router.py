from fastapi_users import FastAPIUsers

from api.dependencies.auth.backend import authentication_backend
from api.dependencies.auth.user_manager import get_user_manager
from core.models import User
from core.types.user_id import UserIdType

fastapi_users_router = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)
