from django.contrib import admin
from .models import Message, Profiler
from .forms import ProfilerForm


@admin.register(Profiler)
class ProfilerAdmin(admin.ModelAdmin):
    list_display = ("id", "external_id", "name")
    form = ProfilerForm


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "profiler", "text", "created_at")
