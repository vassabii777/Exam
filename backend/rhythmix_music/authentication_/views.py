from rest_framework import status

from django.shortcuts import redirect
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework.generics import RetrieveUpdateAPIView



from .models import User
from .serializers import (
    RegistrationSerializer,
      LoginSerializer,
      UserSerializer,
      
    )

import jwt

from .renderers import UserJSONRenderer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from django.conf import settings
import requests
import urllib.parse




@csrf_exempt
def google_login(request):
    google_auth_url = "https://accounts.google.com/o/oauth2/v2/auth"

    params = {
        "client_id": settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
        "redirect_uri": "http://127.0.0.1:8000/api/v1/google/callback/",  
        "response_type": "code",
        "scope": "email profile",
        "access_type": "offline",
        "prompt": "consent",
    }

    url = f"{google_auth_url}?{urllib.parse.urlencode(params)}"


    return redirect(url)


@csrf_exempt
def google_callback(request):
    code = request.GET.get('code')

    if not code:
        return JsonResponse({"error": "Authorization code not provided"}, status=400)

    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        "code": code,
        "client_id": settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
        "client_secret": settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
        "redirect_uri": "http://127.0.0.1:8000/api/v1/google/callback/",
        "grant_type": "authorization_code",
    }

    token_response = requests.post(token_url, data=token_data)

    if token_response.status_code == 200:
        token_json = token_response.json()
        access_token = token_json.get('access_token')

        # Получение информации о пользователе
        user_info_url = "https://www.googleapis.com/oauth2/v2/userinfo"
        user_info_response = requests.get(user_info_url, headers={"Authorization": f"Bearer {access_token}"})

        if user_info_response.status_code == 200:
            user_info = user_info_response.json()
            email = user_info.get('email')

            # Проверка, существует ли пользователь, используя только email
            user, created = User.objects.get_or_create(
                email=email,
                defaults={'username': email}  # Используем email как username
            )

            # Генерация JWT токена с использованием метода токена модели пользователя
            jwt_token = user.token

            return JsonResponse({"jwt_token": jwt_token})

        return JsonResponse({"error": "Failed to fetch user info from Google"}, status=400)
    

class RegistrationAPIView(APIView):
    """
    Разрешить всем пользователям (аутентифицированным и нет) доступ к данному эндпоинту.
    """
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)



    

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # Обратите внимание, что мы не вызываем метод save() сериализатора, как
        # делали это для регистрации. Дело в том, что в данном случае нам
        # нечего сохранять. Вместо этого, метод validate() делает все нужное.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

    
class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        # Здесь нечего валидировать или сохранять. Мы просто хотим, чтобы
        # сериализатор обрабатывал преобразования объекта User во что-то, что
        # можно привести к json и вернуть клиенту.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        # Паттерн сериализации, валидирования и сохранения - то, о чем говорили
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    




class UploadAvatarView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Avatar uploaded successfully!"})
        return Response(serializer.errors, status=400)