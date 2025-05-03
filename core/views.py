from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, VerificationStatus, Product, Purchase
from .serializers import UserSerializer, VerificationStatusSerializer, ProductSerializer, PurchaseSerializer

class LoginHandleView(APIView):
    def post(self, request):
        handle = request.data.get('handle')
        password = request.data.get('password')
        user = User.objects.filter(handle=handle).first()
        if user and user.check_password(password):
            # Генерируем JWT токены
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Login successful',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class VerifyView(APIView):
    def post(self, request):
        # Логика верификации будет добавлена позже
        return Response({'message': 'Verification endpoint'}, status=status.HTTP_200_OK)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class ShopView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class UserListView(ApiView):
    def get(self, request):
        users = User.objects.filter(is_admin_only=False)  # Исключаем суперадминов
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
