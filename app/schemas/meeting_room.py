# Шаг 13 - создаем модель - pydantic-схему

from typing import Optional

from pydantic import BaseModel, Field, validator


# Базовый класс схемы, от которого наследуем все остальные.
class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]


# Теперь наследуем схему не от BaseModel, а от MeetingRoomBase.
class MeetingRoomCreate(MeetingRoomBase):
    # Переопределяем атрибут name, делаем его обязательным,
    # т.к создавать новый объект без указания name нельзя
    name: str = Field(..., min_length=1, max_length=100)
    # Описывать поле description не нужно: оно уже есть в базовом классе.


# Шаг 24 - новый класс для обновления объектов.
# Обновлять можно каждое поле в отдельности или оба поля сразу,
# поэтому переопределять свойства полей не надо,
# тело класса оставим пустым, потому что в
# базовом классе все поля уже установлены как Optional
class MeetingRoomUpdate(MeetingRoomBase):
    # здесь нужен валидатор, чтобы если поле обязательное поле name будет None,
    # сервер не падал с 500-й ошибкой, а возвращал в ответе ошибку 422 + сообщение
    @validator('name')
    def name_cannot_be_none(cls, value: str):
        if value is None:
            raise ValueError(
                'Имя не может принимать значение None!'
            )
        return value


# Шаг 18 - добавление pydantic-модели для JSON-ответа, который
# будет возвращаться из БД после выполнения запроса
# здесь применено наследование, т.к. схема для запроса и
# схема для ответа имеют общие поля
# Возвращаемую схему унаследуем от MeetingRoomCreate,
# чтобы снова не описывать обязательное поле name.
class MeetingRoomDB(MeetingRoomCreate):
    id: int
    # этот класс нужен для того, чтобы схема могла обработать
    # такой тип данных, как возвращенный из БД объект

    class Config:
        orm_mode = True
