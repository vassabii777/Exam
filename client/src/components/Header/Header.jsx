import React from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { logout } from '../../App/slices/userSlice';
import style from './Header.module.css';
import '@fortawesome/fontawesome-free/css/all.css';

export default function Header() {
    const navigate = useNavigate();
    const dispatch = useDispatch();
    const user = useSelector((state) => state.user.user); 

    const handleLogout = () => {
        dispatch(logout());
        navigate('/login');
    };

    return (
        <header className={style.header}>
            <h1 className={style.logo}>Music</h1>
            <nav className={style.nav}>
                <ul className={style.navList}>
                    <li>
                        <Link to="/">Главная</Link>
                    </li>
                    <li>
                        <Link to="/profile">Профиль</Link>
                    </li>
                    <li className={style.profileSection}>
                        <img
                            // src={user.avatarUrl}
                            alt="Avatar"
                            className={style.avatar}
                        />
                        <span className={style.username}>{user}</span>
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