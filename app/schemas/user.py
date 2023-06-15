from fastapi_users import schemas


# Шаг_37 - создаем схемы для операций с пользователями.
# Благодаря наследованию, в каждой из них сразу получаем
# набор необходимых полей.
class UserRead(schemas.BaseUser[int]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass

