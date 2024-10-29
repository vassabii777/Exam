import spotipy
from spotipy.oauth2   import SpotifyClientCredentials
from tracks.models    import Track
from albums.models    import Album
from artists.models   import Artist
from playlists.models import Playlist



from datetime import timedelta, datetime




sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='6abf45f47ef24595b32d0c4dc7f3fc35',
    client_secret='f0a081d2a4274450ae72687383dfa5db'
))

# импорт Артистов с Spotify
def import_artist_from_spotify(artist_name):
    results = sp.search(q=artist_name, type='artist')

    if not results or not results.get('artists') or not results['artists']['items']:
        return f"Artist {artist_name} not found on Spotify"
    
    artist_data = results['artists']['items'][0]
    spotify_id = artist_data['id']
    

    artist, created = Artist.objects.get_or_create(spotify_id=spotify_id, defaults={
        'name': artist_data['name'],
        'bio': artist_data.get('biography', ''),
        'image': artist_data['images'][0]['url'] if artist_data['images'] else None
    })
    
    return f"Artist {artist.name} imported successfully"


# импорт треков с Spotify
def import_track_from_spotify(track_name):
    results = sp.search(q=track_name, type='track')

    if not results or not results.get('tracks') or not results['tracks']['items']:
        return f"Track {track_name} not found on Spotify"
    
    track_data = results['tracks']['items'][0]
    spotify_id = track_data['id']
    
    # Получаем артиста
    artist_name = track_data['artists'][0]['name']
    artist, _ = Artist.objects.get_or_create(name=artist_name)

    duration_ms = track_data['duration_ms']
    duration = timedelta(milliseconds=duration_ms)

    preview_url = track_data.get('preview_url') 

    print(f"Importing track: {track_data['name']}, preview_url: {preview_url}")


    track, created = Track.objects.get_or_create(
        spotify_id=spotify_id,
        defaults={
            'title': track_data['name'],
            'artist': artist,
            'duration': duration,
            'release_date': track_data['album']['release_date'],
            'preview_url': preview_url  
        }
    )

    return f"Track {track.title} by {artist.name} imported successfully."



# импорт плейлистов
def import_playlist_from_spotify(playlist_name):
    try:
        results = sp.search(q=playlist_name, type='playlist')

        if not results.get('playlists', {}).get('items'):
            return {'error': f"Playlist {playlist_name} not found on Spotify"}

        playlist_data = results['playlists']['items'][0]
        spotify_id = playlist_data['id']
        playlist_title = playlist_data['name']
        playlist_owner = playlist_data['owner']['display_name']

        playlist, created = Playlist.objects.get_or_create(
            spotify_id=spotify_id,
            defaults={'name': playlist_title}
        )

        track_response = sp.playlist_tracks(spotify_id)
        if not track_response.get('items'):
            return {'error': f"No tracks found in the playlist {playlist_name}"}

        for item in track_response['items']:
            track = item.get('track')
            if not track:
                continue

            artist_name = track['artists'][0]['name']
            artist, _ = Artist.objects.get_or_create(name=artist_name)

            album_title = track['album']['name']
            release_date = track['album'].get('release_date')

            if release_date:
                if len(release_date) == 4:
                    release_date += '-01-01' 
                
                try:
                    release_date = datetime.strptime(release_date, '%Y-%m-%d').date()
                except ValueError:
                    return {'error': f"Invalid release date format: {release_date}"}

            album, _ = Album.objects.get_or_create(
                title=album_title,
                artist=artist,
                defaults={'release_date': release_date}
            )
            
            duration = timedelta(milliseconds=track['duration_ms'])

            track_instance, _ = Track.objects.get_or_create(
                spotify_id=track['id'],
                defaults={
                    'title': track['name'],
                    'artist': artist,
                    'album': album,
                    'duration': duration,
                    'preview_url': track.get('preview_url'),
                    'release_date': release_date,
                }
            )

            playlist.tracks.add(track_instance)

        return {
            'message': f"Playlist '{playlist_title}' by {playlist_owner} imported successfully."
        }

    except Exception as e:
        return {'error': f"An error occurred: {str(e)}"}
    

    
# импорт альбомов с Spotify
def import_album_from_spotify(album_name):
    results = sp.search(q=album_name, type='album')

    if not results or not results.get('albums') or not results['albums']['items']:
        return f"Album {album_name} not found on Spotify"
    
    album_data = results['albums']['items'][0]
    spotify_id = album_data['id']
    
    # Получаем артиста
    artist_name = album_data['artists'][0]['name']
    artist, _   = Artist.objects.get_or_create(name=artist_name)

    # Сохраняем альбом в базу данных
    album, created = Album.objects.get_or_create(
        spotify_id =spotify_id,
        defaults={
            'title':  album_data['name'],
            'artist': artist,
            'release_date': album_data['release_date']
        }
    )

    return f"Album {album.title} by {artist.name} imported successfully."

