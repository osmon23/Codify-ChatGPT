from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text',
        'time'
    )
    search_fields = (
        'id',
    )
    exclude = (
        'time',
    )
