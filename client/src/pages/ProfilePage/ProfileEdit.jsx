import React, { useState } from "react";
import InputField from "../../components/UI/InputField";
import style from "./ProfilePage.module.css";

function ProfileEdit({ profileData, onSave }) {
    const [formData, setFormData] = useState({ ...profileData });

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSave = () => {
        onSave(formData);
    };

    return (
        <div className={style.editForm}>
            <InputField
                label="Имя"
                type="text"
                name="name"
                value={formData.name}
                onChange={handleInputChange}
                required
            />
            <InputField
                label="Род занятий"
                type="text"
                name="occupation"
                value={formData.occupation}
                onChange={handleInputChange}
                required
            />
            <InputField
                label="Местоположение"
                type="text"
                name="location"
                value={formData.location}
                onChange={handleInputChange}
                required
            />
            <InputField
                label="Email"
                type="email"
                name="email"
                value={formData.email}
                onChange={handleInputChange}
                required
            />
            <InputField
                label="Дата рождения"
                type="date"
                name="birthdate"
                value={formData.birthdate}
                onChange={handleInputChange}
                required
            />
            <InputField
                label="Аватар URL"
                type="text"
                name="avatarUrl"
                value={formData.avatarUrl}
                onChange={handleInputChange}
                required
            />
            <button className={style.saveButton} onClick={handleSave}>
                Сохранить
            </button>
        </div>
    );
}

export default ProfileEdit;