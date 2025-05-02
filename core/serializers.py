from rest_framework import serializers
from .models import User, VerificationStatus, Product, Purchase

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'handle', 'badge', 'fluency', 'location', 'image', 'enlisted', 'display', 'website']

class VerificationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationStatus
        fields = ['status']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'image', 'category']

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id', 'from_user', 'to_user', 'amount', 'item', 'timestamp', 'source']
