import React from 'react';
import style from './HomePage.module.css';

export default function HomePage() {
    return (
        <div className={style.homePage}>

            {/* Основной контент с плейлистами */}
            <main className={style.mainContent}>
                {/* Секция с плеером */}
                <section className={style.playerSection}>
                    <div className={style.playerContainer}>
                        <div className={style.nowPlaying}>
                            <h2>Now Playing</h2>
                            <div className={style.songDetails}>
                                <img src="song-cover.jpg" alt="Song Cover" className={style.songCover} />
                                <div className={style.songInfo}>
                                    <h3>Song Title</h3>
                                    <p>Artist Name</p>
                                </div>
                            </div>
                        </div>
                        <div className={style.controls}>
                            {/* Здесь будут кнопки управления */}
                            <button className={style.controlButton}>⏮</button>
                            <button className={style.controlButton}>⏯</button>
                            <button className={style.controlButton}>⏭</button>
                        </div>
                    </div>
                </section>

                {/* Секция с плейлистами */}
                <section className={style.playlistsSection}>
                    <h2>Playlists</h2>
                    <div className={style.playlistGrid}>
                        <div className={style.playlistCard}>
                            <img src="playlist-cover1.jpg" alt="Playlist Cover" />
                            <h3>Steampunk Classics</h3>
                        </div>
                        <div className={style.playlistCard}>
                            <img src="playlist-cover2.jpg" alt="Playlist Cover" />
                            <h3>Mechanical Beats</h3>
                        </div>
                        <div className={style.playlistCard}>
                            <img src="playlist-cover3.jpg" alt="Playlist Cover" />
                            <h3>Retro Futurism</h3>
                        </div>
                    </div>
                </section>

                {/* Секция с трендами и избранным */}
                <section className={style.otherSection}>
                    <div className={style.trendingSection}>
                        <h2>Trending</h2>
                        <div className={style.trendingGrid}>
                            <div className={style.trendingCard}>
                                <h3>Song 1</h3>
                                <p>Artist 1</p>
                            </div>
                            <div className={style.trendingCard}>
                                <h3>Song 2</h3>
                                <p>Artist 2</p>
                            </div>
                            <div className={style.trendingCard}>
                                <h3>Song 3</h3>
                                <p>Artist 3</p>
                            </div>
                        </div>
                    </div>

                    <div className={style.favoritesSection}>
                        <h2>Favorites</h2>
                        <div className={style.favoritesGrid}>
                            <div className={style.favoriteCard}>
                                <h3>Favorite 1</h3>
                            </div>
                            <div className={style.favoriteCard}>
                                <h3>Favorite 2</h3>
                            </div>
                            <div className={style.favoriteCard}>
                                <h3>Favorite 3</h3>
                            </div>
                        </div>
                    </div>
                </section>
            </main>

          
        </div>
    );
}