import { useState } from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import axiosInstance from "../../utils/axios";
import { setUser } from "../../App/slices/userSlice";
import style from "./Auth.module.css";
import InputField from "../../components/UI/InputField";

function LoginPage() {
    const [formData, setFormData] = useState({ email: "", password: "" });
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

        const data = { user: { email: formData.email, password: formData.password } };

        try {
            const response = await axiosInstance.post("api/v1/users/login/", data);
            const { token, email, username } = response.data;

            localStorage.setItem("token", token);
            localStorage.setItem("user", JSON.stringify({ email, username }));

            dispatch(setUser({ user: { email, username }, token }));
            navigate("/");

            console.log("Аутентификация успешна", response.data);
        } catch (error) {
            const errorMessage = error.response?.data?.detail || error.message || "Ошибка аутентификации.";
            console.error("Ошибка:", errorMessage);
            setError(errorMessage);
        }
    };

    return (
        <div className={style.authPage}>
            <div className={style.welcomeSection}>
                <h2>Добро пожаловать!</h2>
                <p>Войдите в свою учетную запись</p>
                <button className={style.signInButton} onClick={() => navigate("/register")}>Регистрация</button>
            </div>
            <form onSubmit={handleSubmit} className={style.form}>
                <h2>Вход</h2>
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
                {error && <p className={style.error}>{error}</p>}
                <button type="submit" className={style.submitButton}>Вход</button>
            </form>
        </div>
    );
}

export default LoginPage;