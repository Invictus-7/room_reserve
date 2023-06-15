# Объекты, импортированные в __init__.py, становятся доступными уже из самого пакета,
# в котором лежит __init__.py, а не из какого-либо файла.
from .meeting_room import router as meeting_room_router
from .reservation import router as reservation_router
# Шаг_43 - импортируем роутер пользователя в __init__.py
from .user import router as user_router
