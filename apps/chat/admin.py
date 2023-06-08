from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'question',
        'answer',
        'time',
    )
    search_fields = (
        'question',
    )
