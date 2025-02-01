import requests
import allure
import pytest

from api_urls import Urls
from data import Payloads, Errors

class TestCourierLogin:
    @allure.title("Провека авторизации курьера")
    @allure.description("Проверка атворизации курьера")
    def test_login_courier(self):
        payload = Payloads.generate_courier_payload()
        requests.post(Urls.CREATE_COURIER_URL, data=payload)
        response = requests.post(Urls.LOGIN_COURIER_URL, data=payload)
        assert response.status_code == 200, f"Ожидали статус код 200, а получили {response.status_code}"
        assert "id" in response.json()

    @allure.title("Провека авторизации курьера с неверным логином")
    @allure.description("Проверка атворизации курьера с неверным логином")
    def test_login_courier_with_incorrect_login(self):
        payload = {
        "login": "incorrectLogin123123123",
        "password": "1234",
        "firstName": "Dmitry"
        }
        response = requests.post(Urls.LOGIN_COURIER_URL, data=payload)
        assert response.status_code == 404, f"Ожидали статус код 404, а получили {response.status_code}"
        assert response.json().get('message') == Errors.COURIER_LOGIN_FAIL_AUTH, f"Ожидали {Errors.COURIER_LOGIN_FAIL_AUTH}, а получили {response.json().get('message')}"
    
    @allure.title("Проверка логина при отсутсвии обязательных полей")
    @allure.description("Проверка логина при отсутсвии обязательных полей")
    @pytest.mark.parametrize("fields",["login","password"])
    def test_login_without_required_fields(self, fields):
        payload = payload = {
        "login": "Dmitry",
        "password": "1234",
        }
        if fields in payload:
            del payload[fields]
        response = requests.post(Urls.LOGIN_COURIER_URL, data=payload)
        assert response.status_code == 400, f"Ожидали 400, а пришел {response.status_code}"
        assert response.json().get('message') == Errors.COURIER_LOGIN_EMPTY_DATA, f"Ожидали {Errors.COURIER_LOGIN_EMPTY_DATA}, а получили {response.json().get('message')}"

    @allure.title("Провека авторизации с неправильным логином")
    @allure.description("Проверка атворизации курьера с неправильным логином(регистрируем курьера а потом входим не с тем логином)")
    def test_login_courier_with_different_login(self):
        payload_for_register = Payloads.generate_courier_payload()
        payload_for_login = {
        "login": "diffirentLoginForAuth11",
        "password": "1234",
        "firstName": "Dmitry"
        }
        requests.post(Urls.CREATE_COURIER_URL, data=payload_for_register)
        response = requests.post(Urls.LOGIN_COURIER_URL, data=payload_for_login)
        assert response.status_code == 404, f"Ожидали статус код 404, а получили {response.status_code}"
        assert response.json().get('message') == Errors.COURIER_LOGIN_FAIL_AUTH, f"Ожидали {Errors.COURIER_LOGIN_FAIL_AUTH}, а получили {response.json().get('message')}"


    