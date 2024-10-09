import { configureStore } from "@reduxjs/toolkit";
import userReducer, { setUser } from './slices/userSlice';

// Настройка Redux store
const store = configureStore({
    reducer: {
        user: userReducer,
    },
});

// Проверяем токен в localStorage при инициализации приложения
const token = localStorage.getItem("token");
if (token) {
    // Восстанавливаем токен в состоянии Redux
    store.dispatch(setUser({ user: null, token }));
}

export default store;