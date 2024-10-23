import { configureStore } from "@reduxjs/toolkit";
import Cookies from 'js-cookie';

import userReducer, { setUser } from './slices/userSlice';

// Настройка Redux store
const store = configureStore({
    reducer: {
        user: userReducer,
    },
});

// Проверяем токен в куках при инициализации приложения
const token = Cookies.get('token');
if (token) {
    // Восстанавливаем токен в состоянии Redux
    store.dispatch(setUser({ user: null, token }));
}

export default store;