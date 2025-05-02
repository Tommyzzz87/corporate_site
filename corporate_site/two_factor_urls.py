from django.urls import path
from two_factor.views import (
    LoginView,
    ProfileView,
    QRGeneratorView,
    SetupView,
    SetupCompleteView,
    BackupTokensView,
    DisableView,
)

app_name = 'two_factor'

urlpatterns = [
    path('account/login/', LoginView.as_view(), name='login'),
    path('account/two_factor/setup/', SetupView.as_view(), name='setup'),
    path('account/two_factor/qrcode/', QRGeneratorView.as_view(), name='qr'),
    path('account/two_factor/setup/complete/', SetupCompleteView.as_view(), name='setup_complete'),
    path('account/two_factor/backup/tokens/', BackupTokensView.as_view(), name='backup_tokens'),
    path('account/two_factor/', ProfileView.as_view(), name='profile'),
    path('account/two_factor/disable/', DisableView.as_view(), name='disable'),
]
