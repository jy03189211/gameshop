from django.contrib import admin
from .models import (
    User,
    Game,
    Category,
    Order,
    PaymentStub,
    Purchase,
    Savegame,
    Score
)

admin.site.register(User)
admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(PaymentStub)
admin.site.register(Purchase)
admin.site.register(Savegame)
admin.site.register(Score)