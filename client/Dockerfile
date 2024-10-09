# Указываем базовый образ
FROM node:18

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и yarn.lock для установки зависимостей
COPY package.json yarn.lock ./

# Устанавливаем зависимости
RUN yarn install

# Копируем остальные файлы приложения
COPY . .

# Собираем React-приложение
RUN yarn build

# Используем сервер для раздачи статических файлов (например, serve)
RUN yarn global add serve

# Порт для работы сервера
EXPOSE 3000

# Запускаем сервер для отображения скомпилированного приложения
CMD ["serve", "-s", "build"]