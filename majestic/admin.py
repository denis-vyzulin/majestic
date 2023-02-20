from django.contrib import admin
from .models import FeedbackMessage


@admin.register(FeedbackMessage)
class FeedbackMessageAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_send'
    list_display = [
        'fullname',
        'phone',
        'date_send',
    ]
    readonly_fields = [
        'agreement',
    ]
    ordering = ['date_send']