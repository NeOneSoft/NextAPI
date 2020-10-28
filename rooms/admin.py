#Django
from django.contrib import admin
#Model
from .models import Room


@admin.register(Room)
class CommitAdmin(admin.ModelAdmin):
    list_display = ['room_name', 'reserved_date', 'start_time', 'end_time', 'status', 'minutes_estimated',
                    'current_time']
    search_fields = ['room_name']
    list_editable = ['status']
    ordering = ['pk']
