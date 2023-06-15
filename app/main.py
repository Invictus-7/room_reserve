from fastapi import FastAPI

from app.api.routers import main_router
from app.core.config import settings

# Шаг №2 - используем импортированные settings
# в основном файле
# они могут быть перезаписаны из файла .env,
# если в нем заданы переменные с такими же
# именами, как у этих полей
app = FastAPI(title=settings.app_title)  # задаем название приложения из settings

# Шаг 16 - импортируем router в файл с приложением
app.include_router(main_router)
