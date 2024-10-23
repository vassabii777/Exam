FROM python:3.12-slim

WORKDIR /app

# Копируем файл с зависимостями, устанавливаем их и удаляем файл
COPY requirements.txt /app/
RUN pip install -r requirements.txt && rm requirements.txt

# Копируем весь проект
COPY . /app

# Запуск приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

