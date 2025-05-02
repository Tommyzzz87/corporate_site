from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    handle = models.CharField(max_length=255, unique=True)
    badge = models.CharField(max_length=255, blank=True)
    fluency = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    image = models.URLField(blank=True)
    enlisted = models.DateTimeField(null=True, blank=True)
    display = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    discord_id = models.CharField(max_length=255, blank=True)
    telegram_id = models.CharField(max_length=255, blank=True)
    is_banned = models.BooleanField(default=False)

    # Указываем уникальные related_name для устранения конфликта
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='core_user_groups',  # Уникальное имя для обратной связи
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='core_user_permissions',  # Уникальное имя для обратной связи
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
class VerificationStatus(models.Model):
    STATUS_CHOICES = (
        ('Corporate', 'Corporate'),
        ('Affiliate', 'Affiliate'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='departments/')

class Function(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Role(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='roles/')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Position(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='positions/')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    function = models.ForeignKey(Function, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Purchase(models.Model):
    from_user = models.ForeignKey(User, related_name='purchases_from', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='purchases_to', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    item = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=255)

class Reward(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='rewards/')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Ship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ship_name = models.CharField(max_length=255)
    ship_image = models.URLField()
    ship_description = models.TextField()

class CorporationCheckSettings(models.Model):
    sid = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
