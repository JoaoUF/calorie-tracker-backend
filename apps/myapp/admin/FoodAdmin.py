from django.contrib import admin
from apps.myapp.models import Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass
