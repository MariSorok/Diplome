from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from project.models import Booking, Preorder, Dish, Table

@admin.register(Booking)
class BookingAdmin(GuardedModelAdmin):
    pass

@admin.register(Preorder)
class PreorderAdmin(GuardedModelAdmin):
    pass

@admin.register(Dish)
class DishAdmin(GuardedModelAdmin):
    pass

@admin.register(Table)
class TableAdmin(GuardedModelAdmin):
    pass