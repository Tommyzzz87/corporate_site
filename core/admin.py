from django.contrib import admin
from .models import User, VerificationStatus, Department, Function, Role, Position, Category, Product, Purchase, Reward, Ship, CorporationCheckSettings

admin.site.register(User)
admin.site.register(VerificationStatus)
admin.site.register(Department)
admin.site.register(Function)
admin.site.register(Role)
admin.site.register(Position)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Reward)
admin.site.register(Ship)
admin.site.register(CorporationCheckSettings)
