import React from "react";
import style from "./ProfilePage.module.css";

function ProfileView({ profileData, onEdit }) {
    return (
        <div className={style.details}>
            <img
                src={profileData.avatarUrl}
                alt="Avatar"
                className={style.avatar}
            />
            <p><strong>Имя:</strong> {profileData.name}</p>
            <p><strong>Род занятий:</strong> {profileData.occupation}</p>
            <p><strong>Местоположение:</strong> {profileData.location}</p>
            <p><strong>Email:</strong> {profileData.email}</p>
            <p><strong>Дата рождения:</strong> {profileData.birthdate}</p>
            <button className={style.button} onClick={onEdit}>
                Редактировать профиль
            </button>
        </div>
    );
}

export default ProfileView;