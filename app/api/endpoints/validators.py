from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.user import current_superuser, current_user
from app.crud.meeting_room import meeting_room_crud
from app.models.meeting_room import MeetingRoom
from app.models.reservation import Reservation
from app.models import User
from app.crud.reservation import reservation_crud


async def check_name_duplicate(
        room_name: str,
        session: AsyncSession,
) -> None:
    # Замените вызов функции на вызов метода.
    room_id = await meeting_room_crud.get_room_id_by_name(room_name, session)
    if room_id is not None:
        raise HTTPException(
            status_code=422,
            detail='Переговорка с таким именем уже существует!',
        )


async def check_meeting_room_exists(
        meeting_room_id: int,
        session: AsyncSession,
) -> MeetingRoom:
    # Замените вызов функции на вызов метода.
    meeting_room = await meeting_room_crud.get(meeting_room_id, session)
    if meeting_room is None:
        raise HTTPException(
            status_code=404,
            detail='Переговорка не найдена!'
        )
    return meeting_room


# Шаг_35 - создаем корутину-валидатор, которая будет вызывать метод
# проверки занятости переговорок, созданный в тридцать четвертом шаге
async def check_reservation_intersections(**kwargs) -> None:
    reservations = await reservation_crud.get_reservations_at_the_same_time(**kwargs)
    if len(reservations) != 0:
        raise HTTPException(
            status_code=422,
            detail=str(reservations)
        )


async def check_reservation_before_edit(
        reservation_id: int,
        session: AsyncSession,
        # Шаг_51 добавляем проверку на право
        # редактировать/удалять бронь
        user: User
) -> Reservation:
    reservation = await reservation_crud.get(
        # Для понятности кода можно передавать аргументы по ключу.
        obj_id=reservation_id, session=session
    )
    if not reservation:
        raise HTTPException(status_code=404, detail='Бронь не найдена!')
    # Новая проверка и вызов исключения.
    if reservation.user_id != user.id and not user.is_superuser:
        raise HTTPException(
            status_code=403,
            detail='Невозможно редактировать или удалить чужую бронь!'
        )
    return reservation
