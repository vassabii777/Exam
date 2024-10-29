from django.urls import path
from .views import (
    TrackListCreateView,
    TrackRetrieveUpdateDestroyView,
    UserAddTrackPlaylistView,
    UserRemoveTrackFromPlaylistView,
    SpotifyImportTrackView,
)


urlpatterns = [
    path('tracks/', TrackListCreateView.as_view(), name='track-list-create'),
    path('tracks/<uuid:pk>/', TrackRetrieveUpdateDestroyView.as_view(), name='track-detail'),

    path('import-track-spotify/', SpotifyImportTrackView.as_view(), name='import-track-spotify'),

    path('playlists/<uuid:pk>/add-track/', UserAddTrackPlaylistView.as_view(), name='user-add-track'),
    path('playlists/<uuid:pk>/remove-track/', UserRemoveTrackFromPlaylistView.as_view(), name='user-remove-track'),

]