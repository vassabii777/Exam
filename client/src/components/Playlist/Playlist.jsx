import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import Api from '../../api/Api';
import style from './Playlist.module.css';

export default function Playlist({ title, api, route }) {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                let responseData;
                switch (api) {
                    case 'getAllArtists':
                        responseData = await Api.getAllArtists();
                        break;
                    case 'getAllAlbums':
                        responseData = await Api.getAllAlbums();
                        break;
                    case 'getAllTracks':
                        responseData = await Api.getAllTracks();
                        break;
                    case 'getAllPlaylists':
                        responseData = await Api.getAllPlaylists();
                        break;
                    default:
                        throw new Error('Неизвестный API метод');
                }
                setData(responseData);
            } catch (err) {
                setError(err);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, [api]);

    if (loading) {
        return <p className={style.loading}>Загрузка...</p>;
    }

    if (error) {
        return <p className={style.error}>Ошибка при загрузке: {error.message}</p>;
    }

    return (
        <div className={style.playlist}>
            <h2 className={style.title}>{title}</h2>
            {data.length > 0 ? (
                <ul className={style.list}>
                    {data.map((item) => (
                        <li key={item.id} className={style.item}>
                            <Link className={style.link} to={`/${route}/${item.id}`}>
                                {item.title}
                            </Link>
                        </li>
                    ))}
                </ul>
            ) : (
                <p className={style.empty}>Нет доступных данных</p>
            )}
        </div>
    );
}