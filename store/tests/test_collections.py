from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
import pytest

"""
todo:
    list | retrieve::
        - if anonymous user returns 401
        - if not admin returns 403
        - [list] if admin returns 200
        - [retrieve] if admin and invalid id  returns 404
        - [retrieve] if admin and valid id  returns 200
        

    create | update | delete:
        - if anonymous user returns 401
        - if not admin returns 403
        - if admin returns 201
    
    
"""


@pytest.fixture
def create_collection(api_client):
    def do_create(collection):
        return api_client.post("/store/collections/", collection)

    return do_create


@pytest.mark.django_db
class TestCreateCollection:

    def test_if_user_is_anonymous_return_401(self, create_collection):
        # Arrange

        # act
        response = create_collection({"title": "A"})
        # assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_return_403(self, api_client):

        api_client.force_authenticate(user={})
        response = api_client.post("/store/collections/", {"title": "A"})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_admin_and_invalid_data_return_400(self, api_client):
        api_client.force_authenticate(user=User(is_staff=True))
        response = api_client.post("/store/collections/", {"title": ""})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["title"] is not None

    def test_if_user_is_admin_return_201(self, api_client):
        api_client.force_authenticate(user=User(is_staff=True))
        response = api_client.post("/store/collections/", {"title": "A"})
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"] > 0
