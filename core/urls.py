from django.urls import path
from . import views

urlpatterns = [
    path('login-handle/', views.LoginHandleView.as_view(), name='login-handle'),
    path('verify/', views.VerifyView.as_view(), name='verify'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('shop/', views.ShopView.as_view(), name='shop'),
]
