import React from 'react';
import style from './HomePage.module.css';
import { Link } from 'react-router-dom';

import Playlist from '../../components/Playlist/Playlist';
import TrackInfo from '../../components/TrackInfo/TrackInfo';

export default function HomePage() {
    return (
        <div className={style.container}>
            <div className={style.main}>
                <Playlist />
                <Playlist />
                <Playlist />
            </div>
            <div className={style.TrackInfo}>
                <TrackInfo />
            </div>
        </div>
    );
}

