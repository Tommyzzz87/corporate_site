from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Category, CategoryCheckSettings, Component, Position, Product, Purchase, Reward, Role, Ship, VerificationStatus

class UserAdmin(BaseUserAdmin):
    list_display = ('handle', 'email', 'is_admin_only', 'is_staff', 'is_superuser')
    list_filter = ('is_admin_only', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('handle', 'email', 'password')}),
        ('Personal info', {'fields': ('badge', 'fluency', 'location', 'image', 'enlisted', 'display', 'website')}),
        ('Permissions', {'fields': ('is_admin_only', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('handle', 'email', 'password1', 'password2', 'is_admin_only', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('handle', 'email')
    ordering = ('handle',)
    filter_horizontal = ('groups', 'user_permissions',)

    def get_queryset(self, request):
        # Исключаем пользователей с is_admin_only=True из списка
        qs = super().get_queryset(request)
        return qs.filter(is_admin_only=False)

# Регистрация моделей
admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(CategoryCheckSettings)
admin.site.register(Component)
admin.site.register(Position)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Reward)
admin.site.register(Role)
admin.site.register(Ship)
admin.site.register(VerificationStatus)
