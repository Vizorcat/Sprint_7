import pytest
import requests
from helpers import create_random_login, create_random_password, create_random_firstname
from config import Urls


@pytest.fixture
def courier_teardown():
    payload = {
        'login': create_random_login(),
        'password': create_random_password(),
        'firstName': create_random_firstname()
    }
    response = requests.post(Urls.URL_courier_create, json=payload)
    assert response.status_code == 201, f"Failed to create courier: {response.json()}"
    courier_id = response.json().get('id')

    yield payload, courier_id

    if courier_id:
        delete_response = requests.delete(f"{Urls.URL_courier_delete}/{courier_id}")
        assert delete_response.status_code == 200, f"Failed to delete courier: {delete_response.json()}"