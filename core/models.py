from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    handle = models.CharField(max_length=150, unique=True)
    badge = models.CharField(max_length=255, blank=True, null=True)
    fluency = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    enlisted = models.DateTimeField(blank=True, null=True)
    display = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    is_admin_only = models.BooleanField(default=False)

    USERNAME_FIELD = 'handle'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.handle

    def can_authenticate(self):
        return self.is_active

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()  # Добавляем поле description

    def __str__(self):
        return self.name

class Component(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)  # Добавляем null=True
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.handle} - {self.product.name}"

class Reward(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Ship(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class VerificationStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.handle} - {self.status}"
