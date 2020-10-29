# Django
from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Djangorestframework
from rest_framework import viewsets

# Models and Serializers
from .models import Room
from .serializers import RoomSerializer, CreateRoomSerializer


# Change status of our room
def room_update(request, pk):
    room = get_object_or_404(Room, pk=pk)
    room.status = 'RESERVED'
    room.save()
    messages.success(request, 'This room was reserved successfully')
    return render(request, 'rooms/rooms.html', {"rooms": Room.objects.all()})


# Frontend Logic
def courses(request):
    context = {
        'rooms': Room.objects.all()
    }
    return render(request, 'rooms/rooms.html', context)


# Room list view
class RoomListView(ListView):
    model = Room
    template_name = 'rooms/rooms.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'rooms'
    ordering = ['id']
    paginate_by = 10


# Data for API-Rest
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    # Over write serializer class
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateRoomSerializer
        return RoomSerializer
