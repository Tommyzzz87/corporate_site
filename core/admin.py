from django.contrib import admin
from .models import (
    Category,
    CorporationCheckSettings,
    Department,
    Function,
    User,
    VerificationStatus,
    Ship,
    Role,
    Reward,
    Purchase,
    Product,
    Position,
)

admin.site.register(Category)
admin.site.register(CorporationCheckSettings)
admin.site.register(Department)
admin.site.register(Function)
admin.site.register(User)
admin.site.register(VerificationStatus)
admin.site.register(Ship)
admin.site.register(Role)
admin.site.register(Reward)
admin.site.register(Purchase)
admin.site.register(Product)
admin.site.register(Position)
