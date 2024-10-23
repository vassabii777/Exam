from django.urls import path
from .views import (
    AlbumListCreateView,
    AlbumRetrieveUpdateDestroyView,

    ArtistListCreateView,
    ArtistRetrieveUpdateDestroyView,

    PlaylistListCreateView,
    PlaylistRetrieveUpdateDestroyView,

    TrackListCreateView,
    TrackRetrieveUpdateDestroyView,

    SpotifyImportAlbumView,

    ImportPlaylistView,

    SpotifyImportArtistView,

    SpotifyImportTrackView
)

urlpatterns = [
    # Artist URLs
    path('api/v1/artists/', ArtistListCreateView.as_view(), name='artist-list-create'),
    path('api/v1/artists/<uuid:pk>/', ArtistRetrieveUpdateDestroyView.as_view(), name='artist-detail'),

    # Album URLs
    path('api/v1/albums/', AlbumListCreateView.as_view(), name='album-list-create'),
    path('api/v1/albums/<uuid:pk>/', AlbumRetrieveUpdateDestroyView.as_view(), name='album-detail'),

    # Track URLs
    path('api/v1/tracks/', TrackListCreateView.as_view(), name='track-list-create'),
    path('api/v1/tracks/<uuid:pk>/', TrackRetrieveUpdateDestroyView.as_view(), name='track-detail'),

    # Playlist URLs
    path('api/v1/playlists/', PlaylistListCreateView.as_view(), name='playlist-list-create'),
    path('api/v1/playlists/<uuid:pk>/', PlaylistRetrieveUpdateDestroyView.as_view(), name='playlist-detail'),



    # Import URLs
    path('api/v1/import-artist-spotify/', SpotifyImportArtistView.as_view(), name='import-artist-spotify'),

    path('api/v1/import-track-spotify/', SpotifyImportTrackView.as_view(), name='import-track-spotify'),

    path('api/v1/import-album-spotify/', SpotifyImportAlbumView.as_view(), name='import-album-spotify'),

    path('api/v1/import-playlist-spotify/', ImportPlaylistView.as_view(), name='import-playlist-spotify'),
]