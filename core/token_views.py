from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework import serializers

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Получаем модель пользователя
        user_model = get_user_model()

        # Извлекаем данные из запроса
        handle = attrs.get('handle')  # Используем 'handle' напрямую
        password = attrs.get('password')

        # Проверяем, существует ли пользователь с таким handle
        user = user_model.objects.filter(handle=handle).first()

        # Проверяем, существует ли пользователь, активен ли он и верный ли пароль
        if user and user.is_active and user.check_password(password):
            # Генерируем токены
            refresh = RefreshToken.for_user(user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        else:
            raise serializers.ValidationError(
                {'detail': 'No active account found with the given credentials'}
            )

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
