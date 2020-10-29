# Django
from django.conf.urls import url, include
from django.urls import path
from django.test import TestCase

# Djangorestframework
from rest_framework import routers
from rest_framework.test import RequestsClient, APITestCase


# API tests
class BoardsApiTest(APITestCase):
    """ Test API"""
    urlpatterns = [
        path('api/v1/', include('core.urls.v1')),
    ]

    def test_localhost_url(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000')

        self.assertEqual(response.status_code, 200)

    def test_rooms_url(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/api/v1/rooms/')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual('{"id": 1, "room_name": "Room 1"}', '{"id": 1, "room_name": "Room 1"}')

    def test_admin_url(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/admin/')

        self.assertEqual(response.status_code, 200)

    def test_docs_url(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/docs')

        self.assertEqual(response.status_code, 200)
