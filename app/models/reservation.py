from sqlalchemy import Column, DateTime, ForeignKey, Integer

from app.core.db import Base


class Reservation(Base):
    __tablename__ = 'Reservation'  # КОСТЫЛЬ
    id = Column(Integer, primary_key=True)  # КОСТЫЛЬ
    from_reserve = Column(DateTime)
    to_reserve = Column(DateTime)
    # Столбец с внешним ключом: ссылка на таблицу meetingroom, а именно - на ее поле id
    meetingroom_id = Column(Integer, ForeignKey('MeetingRoom.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    # Шаг_36 - добавляем строковое отображение для списка забронированных переговорок
    def __repr__(self):
        return (
            f'Уже забронировано с {self.from_reserve} по {self.to_reserve}'
        )
