import React, { useState } from "react";
import ProfileView from "./ProfileView";
import ProfileEdit from "./ProfileEdit";
import style from "./ProfilePage.module.css";

function ProfilePage() {
    const [isEditing, setIsEditing] = useState(false);
    const [profileData, setProfileData] = useState({
        name: "John Doe",
        occupation: "Adventurer & Inventor",
        location: "London, UK",
        email: "john.doe@example.com",
        birthdate: "1985-08-16",
        avatarUrl: "/logo.png",
    });

    const handleSave = (updatedProfile) => {
        setProfileData(updatedProfile);
        setIsEditing(false);
    };

    const handleEdit = () => {
        setIsEditing(true);
    };

    return (
        <div className={style.pageWrapper}>
            <div className={style.profilePage}>
                <h1 className={style.header}>Мой профиль</h1>
                {isEditing ? (
                    <ProfileEdit profileData={profileData} onSave={handleSave} />
                ) : (
                    <ProfileView profileData={profileData} onEdit={handleEdit} />
                )}
            </div>
        </div>
    );
}

export default ProfilePage;