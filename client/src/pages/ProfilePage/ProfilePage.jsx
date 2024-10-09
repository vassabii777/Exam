import React, { useState } from "react";
import style from "./ProfilePage.module.css";

function ProfilePage() {
    const [isEditing, setIsEditing] = useState(false);
    const [profileData, setProfileData] = useState({
        name: "John Doe",
        occupation: "Adventurer & Inventor",
        location: "London, UK",
        email: "john.doe@example.com",
        birthdate: "1985-08-16",
        avatarUrl: "https://example.com/avatar.jpg",
    });

    const [formData, setFormData] = useState({ ...profileData });

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSave = () => {
        setProfileData({ ...formData });
        setIsEditing(false);
    };

    const handleEdit = () => {
        setIsEditing(true);
    };

    return (
        <div className={style.pageWrapper}>
            <div className={style.profilePage}>
                <h1 className={style.header}>User Profile</h1>

                <img
                    src={profileData.avatarUrl}
                    alt="Avatar"
                    className={style.avatar}
                />

                {isEditing ? (
                    <div className={style.editForm}>
                        <div className={style.inputGroup}>
                            <label>Name:</label>
                            <input
                                type="text"
                                name="name"
                                value={formData.name}
                                onChange={handleInputChange}
                            />
                        </div>
                        <div className={style.inputGroup}>
                            <label>Occupation:</label>
                            <input
                                type="text"
                                name="occupation"
                                value={formData.occupation}
                                onChange={handleInputChange}
                            />
                        </div>
                        <div className={style.inputGroup}>
                            <label>Location:</label>
                            <input
                                type="text"
                                name="location"
                                value={formData.location}
                                onChange={handleInputChange}
                            />
                        </div>
                        <div className={style.inputGroup}>
                            <label>Email:</label>
                            <input
                                type="email"
                                name="email"
                                value={formData.email}
                                onChange={handleInputChange}
                            />
                        </div>
                        <div className={style.inputGroup}>
                            <label>Birthdate:</label>
                            <input
                                type="date"
                                name="birthdate"
                                value={formData.birthdate}
                                onChange={handleInputChange}
                            />
                        </div>
                        <div className={style.inputGroup}>
                            <label>Avatar URL:</label>
                            <input
                                type="text"
                                name="avatarUrl"
                                value={formData.avatarUrl}
                                onChange={handleInputChange}
                            />
                        </div>
                        <button className={style.saveButton} onClick={handleSave}>
                            Save
                        </button>
                    </div>
                ) : (
                    <div className={style.details}>
                        <p>Name: {profileData.name}</p>
                        <p>Occupation: {profileData.occupation}</p>
                        <p>Location: {profileData.location}</p>
                        <p>Email: {profileData.email}</p>
                        <p>Birthdate: {profileData.birthdate}</p>
                        <button className={style.button} onClick={handleEdit}>
                            <i className={`fas fa-cog ${style.steampunkIcon}`}></i>
                            Edit Profile
                        </button>
                    </div>
                )}
            </div>
        </div>
    );
}

export default ProfilePage;