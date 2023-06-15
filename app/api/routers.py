from fastapi import APIRouter

from app.api.endpoints import meeting_room_router, reservation_router, user_router

# принимает роутеры из всех пакетов и затем уходит в файл main.py,
# где подключается к объекту приложения - app.include_router(main_router)
main_router = APIRouter()

main_router.include_router(
    meeting_room_router, prefix='/meeting_rooms', tags=['Meeting Rooms']
)
main_router.include_router(
    reservation_router, prefix='/reservations', tags=['Reservations']
)

# Шаг_44 - подключаем роутер пользователя к главном роутеру
main_router.include_router(user_router)
