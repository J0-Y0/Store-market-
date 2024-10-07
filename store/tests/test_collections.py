import pprint
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from model_bakery import baker
import pytest

"""
todo:
    [x] list 
    [x] retrieve
    [x] create 
    [x] update
    [-] partial update
    [x] delete    
"""


@pytest.fixture
def authenticate(api_client):
    def do_authenticate(is_staff=False):
        return api_client.force_authenticate(User(is_staff=is_staff))

    return do_authenticate


@pytest.fixture
def create_collection(api_client):
    def do_create(collection):
        return api_client.post("/store/collections/", collection)

    return do_create


@pytest.fixture
def make_collection():
    return baker.make("store.Collection")


@pytest.fixture
def delete_collection(api_client):
    def do_delete(collection_id=1):
        return api_client.delete(f"/store/collections/{collection_id}/")

    return do_delete


@pytest.fixture
def update_collection(api_client):

    def do_update(collection_id=1, data={"title": "AAA"}):
        return api_client.put(f"/store/collections/{collection_id}/", data)

    return do_update


@pytest.mark.django_db
class TestCreateCollection:

    def test_if_user_is_anonymous_return_401(self, create_collection):
        # Arrange

        # act
        response = create_collection({"title": "A"})
        # assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_return_403(self, create_collection, authenticate):
        # arrange :setting up the test
        authenticate()
        # act
        response = create_collection({"title": "A"})
        # assert
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_admin_and_invalid_data_return_400(
        self, create_collection, authenticate
    ):
        authenticate(is_staff=True)

        response = create_collection({"title": ""})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["title"] is not None

    def test_if_user_is_admin_return_201(self, create_collection, authenticate):
        authenticate(is_staff=True)

        response = create_collection({"title": "A"})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"] > 0


@pytest.mark.django_db
class TestRetrieveCollection:

    def test_if_collection_exist_return_200(self, api_client, make_collection):
        # arrange
        collection = make_collection
        # act
        response = api_client.get(f"/store/collections/{collection.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == collection.id
        assert response.data["title"] == collection.title

    def test_if_collection_not_exist_return_404(self, api_client):
        response = api_client.get(f"/store/collections/{1}/")
        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestDeleteCollection:
    """
    if
        [x]   anonymous user -> 401
        [x]   non admin user -> 403
        [x]   admin +id not exit-> 404
        [x]   admin +id exit -> 204
    """

    def test_if_user_is_anonymous_return_401(self, delete_collection):
        response = delete_collection()
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_return_403(self, delete_collection, authenticate):
        authenticate()
        response = delete_collection()
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_admin_and_collection_not_exist_return_404(
        self, delete_collection, authenticate
    ):
        authenticate(is_staff=True)
        response = delete_collection()
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_user_is_admin_and_collection_exist_return_204(
        self, delete_collection, authenticate, make_collection
    ):
        collection = make_collection
        authenticate(is_staff=True)
        response = delete_collection(collection.id)
        assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
class TestUpdateCollection:
    """
    Test cases:
    - Anonymous user -> 401 Unauthorized
    - Non-admin user -> 403 Forbidden
    - Admin user:
        - Collection ID does not exist -> 404 Not Found
        - Collection ID exists:
            - Invalid data -> 400 Bad Request->{}
            # - Invalid data types -> 400 Bad Request not works for varchar
            - Missing required fields -> 400 Bad Request
            - Valid data -> 200 OK
    """

    def test_if_user_is_anonymous_return_401(self, update_collection):

        response = update_collection()
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_return_403(self, update_collection, authenticate):

        authenticate()

        response = update_collection()

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_admin_and_collection_not_exist_return_404(
        self, update_collection, authenticate
    ):

        authenticate(is_staff=True)
        response = update_collection()
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_user_is_admin_and_invalid_data_return_400(
        self, update_collection, authenticate, make_collection
    ):

        collection = make_collection
        authenticate(is_staff=True)
        response = update_collection(collection.id, data={"title": ""})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_user_is_admin_and_missing_required_fields_return_400(
        self, update_collection, authenticate, make_collection
    ):

        collection = make_collection
        authenticate(is_staff=True)
        response = update_collection(collection.id, data={})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_user_is_admin_and_valid_data_return_200(
        self, update_collection, authenticate, make_collection
    ):
        collection = make_collection
        authenticate(is_staff=True)
        valid_data = {"title": "Updated Collection Name"}
        response = update_collection(collection.id, data=valid_data)
        assert response.status_code == status.HTTP_200_OK
