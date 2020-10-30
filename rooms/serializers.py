# Djangorestframework
from rest_framework import serializers

# Models
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    """
    Room general purpose serializer
    """

    class Meta:
        model = Room
        fields = ['id', 'room_name', 'reserved_date', 'start_time', 'end_time', 'status', 'minutes_estimated', 'current_time']


class CreateRoomSerializer(serializers.ModelSerializer):
    """
    Create Room serializer
    """

    class Meta:
        model = Room
        fields = ['room_name', 'reserved_date', 'start_time', 'end_time', 'status', 'minutes_estimated', 'current_time']