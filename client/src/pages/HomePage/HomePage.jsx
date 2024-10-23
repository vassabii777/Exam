import React from 'react';
import style from './HomePage.module.css';
import Playlist from '../../components/Playlist/Playlist';
import TrackInfo from '../../components/TrackInfo/TrackInfo';

export default function HomePage() {
    return (
        <div className={style.container}>
            <div className={style.main}>
                <Playlist
                    title="Ваши плейлисты"
                    api="getAllPlaylists"
                    route="playlist"
                />
                <Playlist
                    title="Популярные альбомы"
                    api="getAllAlbums"
                    route="album"
                />
                <Playlist
                    title="Популярные треки"
                    api="getAllTracks"
                    route="track"
                />
            </div>
            <div className={style.trackInfo}>
                <TrackInfo />
            </div>
        </div>
    );
}