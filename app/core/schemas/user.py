from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserIn(UserBase):
    pass


class UserOut(UserBase):
    id: int
    username: str
