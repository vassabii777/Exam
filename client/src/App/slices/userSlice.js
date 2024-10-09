import { createSlice } from "@reduxjs/toolkit";

// Начальное состояние среза пользователя
const initialState = {
    user: null, // Хранит информацию о пользователе
    token: null, // Хранит токен аутентификации
};

const userSlice = createSlice({
    name: "user",
    initialState,
    reducers: {
        // Устанавливает пользователя и токен в состояние
        setUser: (state, action) => {
            state.user = action.payload.user;
            state.token = action.payload.token;
        },
        // Выход из системы: очищает состояние пользователя и токена
        logout: (state) => {
            localStorage.removeItem("token");
            localStorage.removeItem("user");
            state.user = null;
            state.token = null;
        },
    },
});

// Экспортируем действия для использования в компонентах
export const { setUser, logout } = userSlice.actions;

// Экспортируем редюсер для использования в store
export default userSlice.reducer;