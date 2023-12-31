from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.meeting_room import MeetingRoom


# Создаем новый класс, унаследованный от CRUDBase.
class CRUDMeetingRoom(CRUDBase):

    # Преобразуем функцию в метод класса.
    async def get_room_id_by_name(
            # Дописываем параметр self.
            # В качестве альтернативы здесь можно
            # применить декоратор @staticmethod.
            self,
            room_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_room_id = await session.execute(
            select(MeetingRoom.id).where(
                MeetingRoom.name == room_name
            )
        )
        db_room_id = db_room_id.scalars().first()
        return db_room_id


# Объект crud наследуем уже не от CRUDBase,
# а от только что созданного класса CRUDMeetingRoom.
# Для инициализации передаем модель, как и в CRUDBase.
meeting_room_crud = CRUDMeetingRoom(MeetingRoom)


































# # Шаг 14 - создаем объект MeetingRoom и асинхронную сессию работы с БД
#
# from fastapi.encoders import jsonable_encoder
#
# from typing import Optional
#
# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import AsyncSession
#
# # Импортируем sessionmaker из файла с настройками БД.
# from app.core.db import AsyncSessionLocal
# from app.models.meeting_room import MeetingRoom
# from app.schemas.meeting_room import MeetingRoomCreate, MeetingRoomUpdate
#
#
# # Функция работает с асинхронной сессией,
# # поэтому ставим ключевое слово async.
# # В функцию передаём схему MeetingRoomCreate и асинхронный генератор сессий
# async def create_meeting_room(new_room: MeetingRoomCreate, session: AsyncSession) -> MeetingRoom:
#     # Конвертируем объект MeetingRoomCreate в словарь.
#     new_room_data = new_room.dict()
#
#     # Создаём объект модели MeetingRoom.
#     # В параметры передаём пары "ключ=значение", для этого распаковываем словарь.
#     db_room = MeetingRoom(**new_room_data)
#
#     # НАСТРОЙКА АСИНХРОННОГО ОБМЕНА ИНФОРМАЦИЙ С БАЗОЙ ДАННЫХ
#     # Создаём асинхронную сессию через контекстный менеджер.
#     session.add(db_room)
#
#     # Записываем изменения непосредственно в БД.
#     # Так как сессия асинхронная, используем ключевое слово await.
#     await session.commit()
#
#     # Обновляем объект db_room: считываем данные из БД, чтобы получить его id.
#     await session.refresh(db_room)
#     # Возвращаем только что созданный объект класса MeetingRoom.
#     return db_room
#
#
# # Шаг 16 - создаем функцию для проверки - есть ли в БД объект с таким же именем
# async def get_room_id_by_name(room_name: str, session: AsyncSession) -> Optional[int]:
#
#     # Получаем объект класса Result.
#     db_room_id = await session.execute(
#         select(MeetingRoom.id).where(
#             MeetingRoom.name == room_name
#         )
#     )
#     # Извлекаем из него конкретное значение.
#     db_room_id = db_room_id.scalars().first()
#     return db_room_id
#
#
# # Шаг 22 - добавляем crud для получения всех объектов из БД
# async def read_all_rooms_from_db(session: AsyncSession) -> list[MeetingRoom]:
#     all_rooms = await session.execute(select(MeetingRoom))
#     # all возвращает список кортежей, a scalars берет из каждого
#     # кортежа первый объект
#     result = all_rooms.scalars().all()
#     return result
#
#
# # Шаг 25 - добавляем crud для получения объекта по ID -
# # он нам будет нужен для того, чтобы перед обновлением или
# # удалением объекта проверить, а есть ли вообще такой объект в базе
# # (что как раз и проверяется по ID)
# async def get_meeting_room_by_id(room_id: int, session: AsyncSession) -> Optional[MeetingRoom]:
#     room_by_id = await session.execute(select(MeetingRoom).where(MeetingRoom.id == room_id))
#     # метод execute вернул список кортежей - обработаем его методами scalars и first
#     db_room = room_by_id.scalars().first()
#     return db_room
#
#
# # Шаг 26 - добавляем функцию для обновления объекта
# async def update_meeting_room(db_room: MeetingRoom,
#                               room_in: MeetingRoomUpdate,
#                               session: AsyncSession,) -> MeetingRoom:
#     # полученный по id объект переводим в словарь
#     convert_got_from_db_to_json = jsonable_encoder(db_room)
#     # данные из запроса на изменение объекта также переводим в словарь
#     update_data = room_in.dict(exclude_unset=True)
#     # сравниваем два объекта выше при помощи цикла for - если есть разница,
#     # то обновляем существующий объект
#     for field in convert_got_from_db_to_json:
#         if field in update_data:
#             setattr(db_room, field, update_data[field])
#     # Завершаем функцию проработкой сессии
#     session.add(db_room)
#     await session.commit()
#     await session.refresh(db_room)
#     return db_room
#
#
# # Шаг 30 - создаем функцию для удаления объекта из БД
# async def delete_meeting_room(
#         db_room: MeetingRoom,
#         session: AsyncSession,
# ) -> MeetingRoom:
#     # Удаляем объект из БД.
#     await session.delete(db_room)
#     # Фиксируем изменения в БД.
#     await session.commit()
#     # Не обновляем объект через метод refresh(),
#     # следовательно он всё ещё содержит информацию об удаляемом объекте.
#     return db_room


