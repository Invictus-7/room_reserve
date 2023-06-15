# хранит код, ответственный за подключение к БД

# Шаг №6 - прописываем все настройки для базы данных
from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from app.core.config import settings


class PreBase:

    @declared_attr
    def __tablename__(cls):
        # Именем таблицы будет название модели в нижнем регистре.
        return cls.__name__.lower()

    # Во все таблицы будет добавлено поле ID.
    id = Column(Integer, primary_key=True)


Base = declarative_base(PreBase)

# создает движок с настройкой на нашу БД
# значение в скобках, по факту, притащит за собой переменную из .env файла
engine = create_async_engine(settings.database_url)
# создается объекта для работы с множественными сессиями
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


# Шаг 20 - создаем асинхронный генератор сессий.
async def get_async_session():
    # Через асинхронный контекстный менеджер и sessionmaker
    # открывается сессия.
    async with AsyncSessionLocal() as async_session:
        # Генератор с сессией передается в вызывающую функцию.
        yield async_session
        # Когда HTTP-запрос отработает - выполнение кода вернётся сюда,
        # и при выходе из контекстного менеджера сессия будет закрыта.

