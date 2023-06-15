from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.endpoints.validators import (
                                          check_meeting_room_exists,
                                          check_reservation_intersections
                                        )
from app.core.db import get_async_session
from app.core.user import current_user, current_superuser
from app.models import User
from app.crud.reservation import reservation_crud
from app.schemas.reservation import ReservationCreate, ReservationDB, ReservationUpdate
from .validators import check_reservation_before_edit


router = APIRouter()


# Шаг_47 - дополняем эндпоинт бронирования моделью пользователя
@router.post('/', response_model=ReservationDB)
async def create_reservation(
        reservation: ReservationCreate,  # передаем схему
        session: AsyncSession = Depends(get_async_session),
        # Получаем текущего пользователя и сохраняем в переменную user.
        user: User = Depends(current_user)

):
    await check_meeting_room_exists(reservation.meetingroom_id, session)
    await check_reservation_intersections(**reservation.dict(), session=session)
    # Передаём объект пользователя в метод создания объекта бронирования.
    new_reservation = await reservation_crud.create(reservation, session, user)

    return new_reservation


# Не забывать указывать list в аннотации возвращаемого ответа,
# иначе в Swagger будет Internal Server Error 500
@router.get('/', response_model=list[ReservationDB], dependencies=[Depends(current_superuser)])
async def get_all_reservations(
        session: AsyncSession = Depends(get_async_session)
):
    """Только для суперюзеров (см. декоратор)."""
    # метод получения всех объектов уже был ранее написан в классе CRUDBase
    # им и воспользуемся
    all_reservations = await reservation_crud.get_multi(session)
    return all_reservations


@router.delete('/{reservation_id}', response_model=ReservationDB)
async def delete_reservation(
        reservation_id: int,
        session: AsyncSession = Depends(get_async_session),
        # Новая зависимость для эндпоинта, которая ниже передается в валидатор
        user: User = Depends(current_user)
):
    reservation = await check_reservation_before_edit(reservation_id, session, user)
    reservation = await reservation_crud.remove(reservation, session)

    return reservation


@router.patch('/{reservation_id}', response_model=ReservationDB)
async def update_reservation(
        reservation_id: int,
        obj_in: ReservationUpdate,
        session: AsyncSession = Depends(get_async_session),
        # Новая зависимость для эндпоинта, которая ниже передается в валидатор
        user: User = Depends(current_user),
):
    # Проверяем, что такой объект бронирования вообще существует.
    reservation = await check_reservation_before_edit(
        reservation_id, session, user
    )
    # Проверяем, что нет пересечений с другими бронированиями.
    await check_reservation_intersections(
        # Новое время бронирования, распакованное на ключевые аргументы.
        **obj_in.dict(),
        # id обновляемого объекта бронирования,
        reservation_id=reservation_id,
        # id переговорки.
        meetingroom_id=reservation.meetingroom_id,
        session=session
    )
    reservation = await reservation_crud.update(
        db_obj=reservation,
        # На обновление передаем объект класса ReservationUpdate, как и требуется.
        obj_in=obj_in,
        session=session,
    )
    return reservation


@router.get('/my_reservations',
            response_model=list[ReservationDB],
            response_model_exclude={'user_id'}
            )
async def get_my_reservations(
        # добавляем обрабоку запросов относительно текущего пользователя
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session)):
    """Получает список всех бронирований для текущего пользователя."""
    reservations = await reservation_crud.get_by_user(session=session, user=user)
    return reservations
