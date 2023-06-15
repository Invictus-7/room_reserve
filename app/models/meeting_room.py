# Шаг №7 - создаем модель

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.core.db import Base


class MeetingRoom(Base):
    __tablename__ = 'MeetingRoom'  # КОСТЫЛЬ
    name = Column(String(100), unique=True, nullable=False)
    id = Column(Integer, primary_key=True)  # КОСТЫЛЬ
    description = Column(Text)
    # Устанавливаем связь между моделями через функцию relationship.
    reservations = relationship('Reservation', cascade='delete')

