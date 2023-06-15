# Шаг 32 - сводим модели в одной точке, чтобы при
# работе с ForeignKey они "знали" друг о друге
from .meeting_room import MeetingRoom
from .reservation import Reservation
# Шаг_39 Чтобы SQLAlchemy узнала обо всех моделях до того,
# как начнутся выстраиваться взаимосвязи между ними,
# импортируем модель User в файл __init__.py
from .user import User

