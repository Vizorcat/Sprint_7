import requests
import allure
import pytest
from data import Data
from config import Urls
from helpers import create_random_login, create_random_password, create_random_firstname


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

class TestCourierCreate:

    @allure.title('Создание аккаунта курьера с валидными данными')
    @allure.description('Код и тело ответа.')
    def test_create_courier_account_success(self, courier_teardown):
        payload, courier_id = courier_teardown
        response = requests.post(Urls.URL_courier_create, json=payload)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}. Response: {response.text}"
        assert response.json() == {'ok': True}, f"Unexpected response body: {response.json()}"

    @allure.title('Ошибка при повторном использовании логина для создания курьера')
    @allure.description('Код и тело ответа.')
    def test_create_courier_account_login_taken_conflict(self, courier_teardown):
        payload, _ = courier_teardown

        response = requests.post(Urls.URL_courier_create, json=payload)
        assert response.status_code == 409, f"Expected 409, got {response.status_code}. Response: {response.text}"
        assert response.json().get(
            'message') == 'Этот логин уже используется', f"Unexpected response body: {response.json()}"

    @allure.title('Ошибка при создании курьера с незаполненными обязательными полями')
    @allure.description('В тест по очереди передаются наборы данных с пустым логином или паролем. '
                        'Код и тело ответа.')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password(), 'firstName': create_random_firstname()},
        {'login': create_random_login(), 'password': '', 'firstName': create_random_firstname()}
    ])
    def test_create_courier_account_with_empty_required_fields(self, empty_credentials):
        response = requests.post(Urls.URL_courier_create, json=empty_credentials)
        assert response.status_code == 400, f"Expected 400, got {response.status_code}. Response: {response.text}"
        assert response.json().get(
            'message') == 'Недостаточно данных для создания учетной записи', f"Unexpected response body: {response.json()}"