import React from 'react';
import style from './Footer.module.css';

export default function Footer() {
    return (
        <footer className={style.footer}>
            <div className={style.audioPlayer}>
                <audio controls>
                    <source src="your-audio-file.mp3" type="audio/mp3" />
                    Your browser does not support the audio element.
                </audio>
            </div>
            <p>&copy; 2024 - Rhythmix. Все права защищены.</p>
        </footer>
    );
}