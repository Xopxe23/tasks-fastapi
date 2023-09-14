from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    class Config:
        from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
