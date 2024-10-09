from django.urls import path

from .views import (LoginAPIView,
                    RegistrationAPIView, 
                    UserRetriveUpdateAPIView,
                    google_login,
                    google_callback)

urlpatterns = [
    path('api/v1/user',UserRetriveUpdateAPIView.as_view()), # редактирование
    path('api/v1/users/',RegistrationAPIView.as_view()), # регистрация
    path('api/v1/users/login/', LoginAPIView.as_view()),  # вход
    path('api/v1/google/login/', google_login, name='google_login'),  # вход с помощью google
    path('api/v1/google/callback/', google_callback, name='google_callback'),  # вход с помощью google
]
