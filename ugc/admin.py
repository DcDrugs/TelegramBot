from django.contrib import admin
from .models import Item, Profiler
from .forms import ProfilerForm


@admin.register(Profiler)
class ProfilerAdmin(admin.ModelAdmin):
    list_display = ("id", "external_id", "name")
    form = ProfilerForm


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "profiler", "name", "cost", "created_at")
