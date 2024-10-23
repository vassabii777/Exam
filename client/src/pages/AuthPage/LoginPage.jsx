import { useState } from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import { setUser } from "../../App/slices/userSlice";
import Cookies from 'js-cookie';
import axiosInstance from "../../utils/axios";
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
            const response = await axiosInstance.post("users/login/", data);
            const { token, email, username, avatar_urls } = response.data;

            Cookies.set("token", token, { expires: 7, secure: true, sameSite: 'Strict' });

            localStorage.setItem("user", JSON.stringify({ email, username, avatarUrl: avatar_urls }));

            dispatch(setUser({ user: { email, username, avatar_urls } }));
            navigate("/");

            console.log("Аутентификация успешна", response.data);

        } catch (error) {
            const errorMessage = error.response?.data?.detail || "Неправильные email или пароль.";
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