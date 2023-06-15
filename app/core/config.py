from pydantic import BaseSettings

# Шаг №1 - описываем настройки проекта;
# они связаны с файлом .env и, в целом,
# являются неким аналогом settings.py
# в других фреймворках


class Settings(BaseSettings):
    # этот класс будет считывать все поля из .env;
    # для этого названия его атрибутов должны быть
    # одинаковы с теми переменными, которые лежат
    # в .env файле; если название не совпадает -
    # то вернется значение по умолчанию; если же
    # и его нет - вернется ошибка
    app_title: str = 'Бронирование переговорок'  # ("Бронирование..." - это значение по умолчанию)
    # Шаг №5 - создаем атрибут database_url, чтобы из файла .env подключилась база
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'  # ЭТО КОСТЫЛЬ!
    secret: str = 'SECRET'  # Должно хранится в .env

    class Config:
        # указываем, из какого файла брать переменные окружения
        env_file = '../.env'


# создаем из наших настроек переменную, чтобы потом
# импортировать ее в рамках проекта туда, куда нам надо
settings = Settings()
