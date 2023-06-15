# Шаг 33 - pydantic-схемы для каждого из CRUD-действий с моделью Reservation

from datetime import datetime, timedelta
from typing import Optional

from pydantic import BaseModel, Extra, Field, root_validator, validator

FROM_TIME = (datetime.now() + timedelta(minutes=10)).isoformat(timespec='minutes')
TO_TIME = (datetime.now() + timedelta(hours=1)).isoformat(timespec='minutes')


# Базовый класс схемы, от которого наследуем все остальные.
class ReservationBase(BaseModel):
    from_reserve: datetime = Field(..., example=FROM_TIME)
    to_reserve: datetime = Field(..., example=TO_TIME)

    class Config:
        # запрет передавать дополнительные поля в запросе
        extra = Extra.forbid


class ReservationUpdate(ReservationBase):
    # добавляем валидаторы времени брони
    @root_validator(skip_on_failure=True)
    def check_from_reserve_before_to_reserve(cls, values):
        reserve_start = values['from_reserve']
        reserve_end = values['to_reserve']
        if reserve_start >= reserve_end:
            raise ValueError(
                'Время окончания бронирования не может быть раньше,'
                'чем время начала бронирования!'
            )
        return values

    @validator('from_reserve')
    def check_from_reserve_later_than_now(cls, value):
        """Проверка на то, чтобы начало бронирования
        не было раньше текущего времени."""
        now = datetime.now()
        if value <= now:
            raise ValueError(
                'Нельзя указывать время раньше, чем текущее'
            )
        return value


# наследуем этот класс от ReservationUpdate для того,
# чтобы два раза не писать валидаторы
class ReservationCreate(ReservationUpdate):
    meetingroom_id: int


class ReservationDB(ReservationBase):
    id: int
    meetingroom_id: int
    # этот класс нужен для того, чтобы схема могла обработать
    # такой тип данных, как возвращенный из БД объект
    # Шаг_49 - дополняем схему ответа для того, чтобы
    # id ТЕКУЩЕГО пользователя возвращался в ответе на запрос
    user_id: Optional[int]

    class Config:
        orm_mode = True

