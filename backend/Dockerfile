# Используем официальный образ Python
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Выполняем миграции
RUN python yandex_music/manage.py migrate

# Открываем порт для приложения
EXPOSE 8000

# Запускаем сервер
CMD ["sh", "-c", "python yandex_music/manage.py migrate && python yandex_music/manage.py runserver 0.0.0.0:8000"]