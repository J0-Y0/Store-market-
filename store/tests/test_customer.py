import pytest
from rest_framework import status
from model_bakery import baker
from authentication.models import User
from store.models import Customer
from django.contrib.auth.models import Permission

"""
    Test cases for CustomerViewSet:
    - Retrieve:
        - Anonymous users: 401 Unauthorized
        - Non-admin users:
            - Without view permission: 403 Forbidden
            - With view permission: 403 Forbidden
        - Admin users:
            - Without view permission: 403 Forbidden
            - With view permission: 200 OK
    - Create:
        - Anonymous users: 401 Unauthorized
        - Non-admin users: 403 Forbidden
        - Admin users:
            - Without permission: 403 Forbidden
            - With permission: 201 Created
    - Delete:
        - Anonymous users: 401 Unauthorized
        - Non-admin users: 403 Forbidden
        - Admin users:
            - Without permission: 403 Forbidden
            - With permission:
                - Invalid ID data type: 400 Bad Request
                - Valid data type but does not exist: 404 Not Found
                - ID exists: 204 No Content
    - Detail:
        - Anonymous users: 401 Unauthorized
        - Non-admin users:
            - Without view permission: 403 Forbidden
            - With view permission: 403 Forbidden
        - Admin users:
            - Without view permission: 403 Forbidden
            - With view permission:
                - Invalid ID data type: 400 Bad Request
                - Valid data type but does not exist: 404 Not Found
                - ID exists: 200 OK
    """


@pytest.fixture
def create_user():
    def do_create(is_staff=False, codenames=None):
        user = User.objects.create_user(
            username="testuser",
            password="password",
            is_staff=is_staff,
        )
        if codenames is not None:
            permissions = Permission.objects.filter(codename__in=codenames)
            user.user_permissions.add(*permissions)
        return user

    return do_create


@pytest.mark.django_db
class TestGetCustomers:

    # Retrieve tests
    def test_if_user_is_anonymous_retrieve_return_401(self, api_client):
        response = api_client.get("/store/customers/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_and_no_view_perm_return_403(
        self, api_client, create_user
    ):
        api_client.force_authenticate(user=create_user())
        response = api_client.get("/store/customers/")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_not_admin_and_has_view_perm_return_403(
        self, api_client, create_user
    ):
        api_client.force_authenticate(user=create_user(codenames=["view_customer"]))
        response = api_client.get("/store/customers/")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_admin_and_no_view_perm_return_403(
        self, api_client, create_user
    ):
        api_client.force_authenticate(user=create_user(is_staff=True))
        response = api_client.get("/store/customers/")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_admin_and_has_view_perm_return_200(
        self, api_client, create_user
    ):
        api_client.force_authenticate(
            user=create_user(is_staff=True, codenames=["view_customer"])
        )
        response = api_client.get("/store/customers/")
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestUpdateCustomer:
    def test_if_user_is_anonymous_update_return_401(self, api_client):
        response = api_client.put("/store/customers/1/", data={"name": "New Customer"})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_update_return_403(self, api_client, create_user):
        api_client.force_authenticate(user=create_user())
        response = api_client.put("/store/customers/1/", data={"name": "New Customer"})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_admin_update_without_permission_return_403(
        self, api_client, create_user
    ):
        api_client.force_authenticate(user=create_user(is_staff=True))
        response = api_client.patch(
            "/store/customers/1/", data={"name": "New Customer"}
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_admin_update_with_permission_return_200(
        self, api_client, create_user
    ):
        api_client.force_authenticate(
            user=create_user(
                is_staff=True, codenames=["change_customer", "view_customer"]
            )
        )

        user = baker.make(User)

        customer = Customer.objects.get(user=user)
        response = api_client.put(
            f"/store/customers/{customer.id}/",
            data={"user": user.id, "phone": "0910804"},
        )

        assert response.status_code == status.HTTP_200_OK
        # assert customer.phone == "0910805134"


@pytest.mark.django_db
class TestCustomerRetrieve:
    # Detail tests
    def test_if_user_is_anonymous_detail_return_401(self, api_client):
        response = api_client.get(f"/store/customers/1/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_detail_return_403(self, api_client, create_user):
        user = baker.make(User)
        api_client.force_authenticate(user=create_user())
        response = api_client.get(f"/store/customers/{user.customer.id}/")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_admin_detail_return_403(self, api_client, create_user):
        user = baker.make(User)
        api_client.force_authenticate(user=create_user(is_staff=True))
        response = api_client.get(f"/store/customers/{user.customer.id}/")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_admin_with_view_perm_and_nonexistent_id_return_404(
        self, api_client, create_user
    ):
        api_client.force_authenticate(
            user=create_user(is_staff=True, codenames=["view_customer"])
        )
        response = api_client.get(
            "/store/customers/9999/"
        )  # Assuming this ID does not exist
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_user_is_admin_with_view_perm_and_existing_id_return_200(
        self, api_client, create_user
    ):
        user = baker.make(User)
        api_client.force_authenticate(
            user=create_user(is_staff=True, codenames=["view_customer"])
        )
        response = api_client.get(f"/store/customers/{user.customer.id}/")
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestDeleteCustomer:
    def test_if_user_is_anonymous_delete_return_401(self, api_client):
        user = baker.make(User)
        response = api_client.delete(f"/store/customers/{user.customer.id}/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_delete_return_403(self, api_client, create_user):
        api_client.force_authenticate(user=create_user())
        user = baker.make(User)
        response = api_client.delete(f"/store/customers/{user.customer.id}/")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_admin_delete_without_permission_return_403(
        self, api_client, create_user
    ):
        api_client.force_authenticate(user=create_user(is_staff=True))
        user = baker.make(User)
        response = api_client.delete(f"/store/customers/{user.customer.id}/")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_admin_delete_with_nonexistent_id_return_404(
        self, api_client, create_user
    ):
        api_client.force_authenticate(
            user=create_user(is_staff=True, codenames=["delete_customer"])
        )
        response = api_client.delete(
            "/store/customers/9999/"
        )  # Assuming this ID does not exist
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_user_is_admin_delete_with_existing_id_return_204(
        self, api_client, create_user
    ):
        api_client.force_authenticate(
            user=create_user(is_staff=True, codenames=["delete_customer"])
        )
        user = baker.make(User)
        response = api_client.delete(f"/store/customers/{user.customer.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
