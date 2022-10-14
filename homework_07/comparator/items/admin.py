from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description"
    list_display_links = "pk", "name"
    ordering = "pk",
