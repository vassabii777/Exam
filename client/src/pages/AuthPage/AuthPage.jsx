import { useState } from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import axiosInstance from "../../utils/axios";
import { setUser } from "../../App/slices/userSlice";
import style from "./AuthPage.module.css";

function AuthPage() {
    const [formData, setFormData] = useState({
        email: "",
        password: "",
        confirmPassword: "",
        username: "",
    });
    const [error, setError] = useState(null);
    const [isLogin, setIsLogin] = useState(true);
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({ ...prevData, [name]: value }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);

        if (!isLogin && formData.password !== formData.confirmPassword) {
            setError("Пароли не совпадают");
            return;
        }

        const url = isLogin ? "api/v1/users/login/" : "api/v1/users/";
        const data = isLogin
            ? { user: { email: formData.email, password: formData.password } }
            : { user: { username: formData.username, email: formData.email, password: formData.password } };

        try {
            const response = await axiosInstance.post(url, data);
            const { token, email, username } = response.data;

            // Сохраняем токен и данные пользователя в Local Storage
            localStorage.setItem("token", token);
            localStorage.setItem("user", JSON.stringify({ email, username }));

            // Обновляем состояние пользователя в Redux
            dispatch(setUser({ user: { email, username }, token }));

            // Перенаправляем пользователя на главную страницу
            navigate("/");

            console.log("Аутентификация успешна", response.data);
            
        } catch (error) {
            const errorMessage = error.response?.data?.detail || error.message || "Ошибка аутентификации. Попробуйте снова.";
            console.error("Ошибка аутентификации:", errorMessage);
            setError(errorMessage);
        }
    };

    return (
        <div className={style.authPage}>
            <h2>{isLogin ? "Вход" : "Регистрация"}</h2>
            <form onSubmit={handleSubmit} className={style.form}>
                {!isLogin && (
                    <InputField
                        label="Имя пользователя"
                        type="text"
                        name="username"
                        value={formData.username}
                        onChange={handleInputChange}
                        required={!isLogin}
                    />
                )}
                <InputField
                    label="Email"
                    type="email"
                    name="email"
                    value={formData.email}
                    onChange={handleInputChange}
                    required
                />
                <InputField
                    label="Пароль"
                    type="password"
                    name="password"
                    value={formData.password}
                    onChange={handleInputChange}
                    required
                />
                {!isLogin && (
                    <InputField
                        label="Подтверждение пароля"
                        type="password"
                        name="confirmPassword"
                        value={formData.confirmPassword}
                        onChange={handleInputChange}
                        required={!isLogin}
                    />
                )}
                {error && <p className={style.error}>{error}</p>}
                <button type="submit" className={style.submitButton}>
                    {isLogin ? "Вход" : "Регистрация"}
                </button>
            </form>
            <button className={style.toggleButton} onClick={() => setIsLogin(!isLogin)}>
                {isLogin ? "Перейти к регистрации" : "Перейти к входу"}
            </button>
        </div>
    );
}

const InputField = ({ label, type, name, value, onChange, required }) => (
    <div className={style.inputGroup}>
        <label>{label}:</label>
        <input
            type={type}
            name={name}
            value={value}
            onChange={onChange}
            required={required}
        />
    </div>
);

export default AuthPage;