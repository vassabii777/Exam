import { useState } from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import axiosInstance from "../../utils/axios";
import { setUser } from "../../App/slices/userSlice";
import style from "./Auth.module.css";
import InputField from "../../components/UI/InputField";

function RegisterPage() {
    const [formData, setFormData] = useState({
        email: "",
        password: "",
        confirmPassword: "",
        username: "",
    });
    const [error, setError] = useState(null);
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({ ...prevData, [name]: value }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);

        if (formData.password !== formData.confirmPassword) {
            setError("Пароли не совпадают");
            return;
        }

        const data = { user: { username: formData.username, email: formData.email, password: formData.password } };

        try {
            const response = await axiosInstance.post("api/v1/users/", data);
            const { token, email, username } = response.data;

            localStorage.setItem("token", token);
            localStorage.setItem("user", JSON.stringify({ email, username }));

            dispatch(setUser({ user: { email, username }, token }));
            navigate("/");

            console.log("Регистрация успешна", response.data);
        } catch (error) {
            const errorMessage = error.response?.data?.detail || error.message || "Ошибка регистрации.";
            console.error("Ошибка:", errorMessage);
            setError(errorMessage);
        }
    };

    return (
        <div className={style.authPage}>
            <form onSubmit={handleSubmit} className={style.form}>
                <h2>Регистрация</h2>
                <InputField
                    label="Имя пользователя"
                    type="text"
                    name="username"
                    value={formData.username}
                    onChange={handleInputChange}
                    required
                    style={style.inputGroup}
                />
                <InputField
                    label="Email"
                    type="email"
                    name="email"
                    value={formData.email}
                    onChange={handleInputChange}
                    required
                    style={style.inputGroup}
                />
                <InputField
                    label="Пароль"
                    type="password"
                    name="password"
                    value={formData.password}
                    onChange={handleInputChange}
                    required
                    style={style.inputGroup}
                />
                <InputField
                    label="Подтверждение пароля"
                    type="password"
                    name="confirmPassword"
                    value={formData.confirmPassword}
                    onChange={handleInputChange}
                    required
                    style={style.inputGroup}
                />
                {error && <p className={style.error}>{error}</p>}
                <button type="submit" className={style.submitButton}>Регистрация</button>
            </form>
            <div className={style.welcomeSection}>
                <h2>Создайте аккаунт</h2>
                <p>Если у вас уже есть аккаунт, войдите</p>
                <button className={style.signInButton} onClick={() => navigate("/login")}>Войти</button>
            </div>
        </div>
    );
}

export default RegisterPage;