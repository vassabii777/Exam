import React from 'react'
import { Link } from 'react-router-dom';

const style = {
    playlist: {
        padding: '20px',
        border: '1px solid #ccc',
        borderRadius: '5px',
        marginBottom: '20px',
        backgroundColor: '#f8f8f8'
    },
    list: {
        listStyle: 'none',
        padding: 0,
        margin: 0
    },
    item: {
        marginBottom: '10px'
    },
    link: {
        textDecoration: 'none',
        color: '#337ab7'
    }
}

export default function Playlist() {
    return (
        <div style={style.playlist}>
            <p>Плейлисты</p>
            <ul style={style.list}>
                <li style={style.item}>
                    <Link style={style.link} to="/playlist/1">Playlist 1</Link>
                </li>
                <li style={style.item}>
                    <Link style={style.link} to="/playlist/2">Playlist 2</Link>
                </li>
                <li style={style.item}>
                    <Link style={style.link} to="/playlist/1">Playlist 1</Link>
                </li>
                <li style={style.item}>
                    <Link style={style.link} to="/playlist/2">Playlist 2</Link>
                </li>
                <li style={style.item}>
                    <Link style={style.link} to="/playlist/1">Playlist 1</Link>
                </li>
                <li style={style.item}>
                    <Link style={style.link} to="/playlist/2">Playlist 2</Link>
                </li>
            </ul>
        </div>
    )
}

