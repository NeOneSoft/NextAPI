# Django
from django.conf.urls import url, include

# Djangorestframework
from rest_framework import routers

# Views
from rooms.views import RoomViewSet

# API urls
router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet),

urlpatterns = [
    url(r'', include(router.urls)),
]