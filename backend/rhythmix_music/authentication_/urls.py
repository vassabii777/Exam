from django.urls import path

from django.conf import settings

from django.conf.urls.static import static

from .views import (RegistrationAPIView, 
                    LoginAPIView,
                    UserRetrieveUpdateAPIView,
                    google_callback,
                    google_login,
                    UploadAvatarView,
)

app_name = 'authentication'
urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path('users/', RegistrationAPIView.as_view(), name='register'),
    path('users/login/', LoginAPIView.as_view(), name='login'),
    path('google/login/', google_login, name='google_login'),
    path('google/callback/', google_callback, name='google_callback'),
    path('users/upload-avatar/', UploadAvatarView.as_view())


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
