## Сервис для бронирования переговорных комнат RoomReserve

### 1. [Общая информация о проекте](#1)
### 2. [База данных и переменные окружения](#2)
### 3. [Команды для запуска](#3)
### 4. [Работа с API](#4)
### 5. [Использованные технологии](#5)
### 6. [Об авторе](#6)

---
### 1. Общая информация о проекте <a id=1></a>

Сервис RoomReserve предоставляет пользователям следующие возможности:
- бронирование переговорной комнаты
- отказ от брони
- предусмотрена роль модератора, имеющего расширенные доступы - может снимать бронь других пользователей


---
### 2. База данных и переменные окружения <a id=2></a>

Проект использует базу данных SQLite.  
Для подключения и выполнения запросов к базе данных необходимо создать и заполнить файл ".env" с переменными окружения в корневой папке проекта.  
Пример:
```bash
APP_TITLE=Сервис бронирования переговорных комнат RoomReserve
DESCRIPTION=Помогает обеспечить проведение важных бизнес-встреч
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=#Здесь напишите Ваш секретный код
```

---
### 3. Команды для запуска <a id=3></a>

Перед запуском необходимо склонировать проект:
```bash
HTTPS: git clone https://github.com/Invictus-7/room_reserve
```

Создать и активировать виртуальное окружение:
```bash
python -m venv venv
```
```bash
Windows: source venv/Scripts/activate
```

Обновить pip и установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Выполнить миграции:
```bash
alembic upgrade head
```

Запустить проект:
```bash
uvicorn app.main:app
```

После запуска проект будет доступен по адресу [http://localhost:8000/](http://localhost:8000/)  
Документация по API проекта доступна можно по адресам:<a id=API></a>
  - Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

---
### 4. Работа с API <a id=4></a>

#### В проекте RoomReserve имеются следующие эндпоинты:
```
under construction

```

---
### 5. Использованные технологии <a id=5></a>

- [Python](https://www.python.org/)
- [FasAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)

---
### 6. Об авторе <a id=6></a>
- [Кирилл Резник](https://github.com/Invictus-7)