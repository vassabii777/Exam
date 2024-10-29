from django.urls import path
from .views import (PlaylistListCreateView,
                    PlaylistRetrieveUpdateDestroyView,
                    UserPlaylistCreateView,
                    UserPlaylistDetailView,
                    SpotifyImportPlaylistView
                    ) 


urlpatterns = [

    # Playlist URLs
    path('playlists/', PlaylistListCreateView.as_view(), name='playlist-list-create'),
    path('playlists/<uuid:pk>/', PlaylistRetrieveUpdateDestroyView.as_view(), name='playlist-detail'),

    path('create-user-playlists/', UserPlaylistCreateView.as_view(), name='user-playlist-create'),
    path('detail-playlists/<uuid:pk>/',UserPlaylistDetailView.as_view(), name='user-playlist-detail'),

    path('import-playlist-spotify/', SpotifyImportPlaylistView.as_view(), name='import-playlist-spotify'),

]