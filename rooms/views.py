# Djangorestframework
from rest_framework import viewsets


# Models and Serializers
from .models import Room
from .serializers import RoomSerializer, CreateRoomSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    # Over write serializer class
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateRoomSerializer
        return RoomSerializer
