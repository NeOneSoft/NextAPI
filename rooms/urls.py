# Django
from django.urls import path

# Views
from .views import RoomListView

# Frontend urls
urlpatterns = [
    path('', RoomListView.as_view(), name='rooms'),
]
