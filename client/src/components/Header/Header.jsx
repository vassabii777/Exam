import React from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { logout } from '../../App/slices/userSlice';
import style from './Header.module.css';
import '@fortawesome/fontawesome-free/css/all.css';

export default function Header() {
    const navigate = useNavigate();
    const dispatch = useDispatch();

    // Обработчик выхода из системы
    const handleLogout = () => {
        dispatch(logout()); // Вызываем действие выхода из системы
        navigate('/login'); // Перенаправляем на страницу входа
    };

    return (
        <header className={style.header}>
            <h1 className={style.logo}>Music</h1>
            <nav className={style.nav}>
                <ul>
                    <li>
                        <Link to="/">Главная</Link>
                    </li>
                    <li>
                        <Link to="/profile">Профиль</Link>
                    </li>
                    <li>
                        <button
                            onClick={handleLogout}
                            className={style.logoutButton}
                            title="Выйти"
                            style={{ background: 'none', border: 'none', cursor: 'pointer' }}
                        >
                            <i className="fas fa-sign-out-alt"></i>
                        </button>
                    </li>
                </ul>
            </nav>
        </header>
    );
}