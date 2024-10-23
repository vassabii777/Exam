import axiosInstance from '../utils/axios';

const apiRequest = async (method, url, data = null) => {
    try {
        const response = await axiosInstance({
            method: method,
            url: url,
            data: data
        });
        return response.data;
    } catch (error) {
        console.error(`Error during ${method.toUpperCase()} request to ${url}:`, error);
        throw error;
    }
};

// Артист 
export const getAllArtists = async () => apiRequest('get', 'artists/');
export const createArtist = async (artist) => apiRequest('post', 'artists/', artist);
export const getArtistById = async (artistId) => apiRequest('get', `artists/${artistId}/`);
export const updateArtist = async (artistId, updatedArtist) => apiRequest('put', `artists/${artistId}/`, updatedArtist);
export const deleteArtist = async (artistId) => apiRequest('delete', `artists/${artistId}/`);

// Альбом
export const getAllAlbums = async () => apiRequest('get', 'albums/');
export const createAlbum = async (album) => apiRequest('post', 'albums/', album);
export const getAlbumById = async (albumId) => apiRequest('get', `albums/${albumId}/`);
export const updateAlbum = async (albumId, updatedAlbum) => apiRequest('put', `albums/${albumId}/`, updatedAlbum);
export const deleteAlbum = async (albumId) => apiRequest('delete', `albums/${albumId}/`);

// Трек
export const getAllTracks = async () => apiRequest('get', 'tracks/');
export const createTrack = async (track) => apiRequest('post', 'tracks/', track);
export const getTrackById = async (trackId) => apiRequest('get', `tracks/${trackId}/`);
export const updateTrack = async (trackId, updatedTrack) => apiRequest('put', `tracks/${trackId}/`, updatedTrack);
export const deleteTrack = async (trackId) => apiRequest('delete', `tracks/${trackId}/`);

// Плейлист
export const getAllPlaylists = async () => apiRequest('get', 'playlists/');
export const createPlaylist = async (playlist) => apiRequest('post', 'playlists/', playlist);
export const getPlaylistById = async (playlistId) => apiRequest('get', `playlists/${playlistId}/`);
export const updatePlaylist = async (playlistId, updatedPlaylist) => apiRequest('put', `playlists/${playlistId}/`, updatedPlaylist);
export const deletePlaylist = async (playlistId) => apiRequest('delete', `playlists/${playlistId}/`);

export default {
    getAllArtists,
    createArtist,
    getArtistById,
    updateArtist,
    deleteArtist,
    getAllAlbums,
    createAlbum,
    getAlbumById,
    updateAlbum,
    deleteAlbum,
    getAllTracks,
    createTrack,
    getTrackById,
    updateTrack,
    deleteTrack,
    getAllPlaylists,
    createPlaylist,
    getPlaylistById,
    updatePlaylist,
    deletePlaylist
};