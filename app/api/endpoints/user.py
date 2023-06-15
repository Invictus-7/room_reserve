# Шаг_42 - настройка роутеров для управления пользователями

# Последний шаг — подключение роутеров через методы класса FastAPIUsers.
# Каждый метод подключает свой роутер; полный список доступных роутеров и
# способы их подключения можно посмотреть в документации.
# Подключаем три роутера:
#
#     аутентификационный роутер (Auth router) — предоставляет доступ к эндпоинтам
#     /login(для аутентификации) и/logout(для завершения сессии)
#     для выбранного бэкенда аутентификации;

#     регистрационный роутер (Register router) —  предоставляет доступ к эндпоинту
#     /register для регистрации нового пользователя;

#     роутер пользователей (Users router) — предоставляет доступ к эндпоинтам управления
#     пользователями (чтение из БД, удаление, обновление).


# Теги и префиксы подключаемых роутеров установлены согласно документации.

# Импортируем и запускаем в работу созданные нами бэкенд и объект класса fastapi_users
from fastapi import APIRouter, HTTPException

from app.core.user import auth_backend, fastapi_users
from app.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter()

router.include_router(
    # В роутер аутентификации
    # передается объект бэкенда аутентификации.
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix='/users',
    tags=['users'],
)


# Шаг_45 - "отключам" эндпоинт удаления пользователей,
# чтобы сделать его невозможным через API
@router.delete(
    # Путь и тег полностью копируют параметры эндпоинта по умолчанию.
    '/users/{id}',
    tags=['users'],
    # Параметр, который показывает, что метод устарел.
    deprecated=True
)
def delete_user(id: str):
    """Не используйте удаление, деактивируйте пользователей."""
    raise HTTPException(
        # 405 ошибка - метод не разрешен.
        status_code=405,
        detail="Удаление пользователей запрещено!"
    )