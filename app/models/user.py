from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer

from app.core.db import Base


# Шаг_38 Создаем модель пользователя
class User(SQLAlchemyBaseUserTable[int], Base):
    # вообще, это свойство должно наследовать, но в данном
    # проекте наследование от Base почему-то не работает
    id = Column(Integer, primary_key=True)
