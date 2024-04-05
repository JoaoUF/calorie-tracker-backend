from django.contrib import admin
from apps.myapp.models import Consume

@admin.register(Consume)
class ConsumeAdmin(admin.ModelAdmin):
    pass