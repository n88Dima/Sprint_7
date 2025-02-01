import requests
import allure
import pytest

from api_urls import Urls
from data import Errors, Payloads

class TestCreatingCourier:

    @allure.title("Создание нового курьера")
    @allure.description("Проверка создания нового курьера, ответа и статус код (должен быть 201)")
    def test_create_new_courier(self, courier):
        assert courier is not None, "Курьер не был создан"

    @allure.title("Проверка создания двух одинаковых курьеров")
    @allure.description("Проверка создания двух одинаковых курьеров, статус 409")
    def test_create_identical_couriers(self, courier):
        response = requests.post(Urls.CREATE_COURIER_URL, data=courier)
        assert response.status_code == 409, f"Ожидали статус 409, а получили {response.status_code}"
        assert response.json().get('message') == Errors.COURIER_ALREADY_CREATED, f"Ожидали сообщение {Errors.COURIER_ALREADY_CREATED}, а получили {response.json().get('message')}"

    @allure.title("Проверка создания курьера без обязательных полей")
    @allure.description("Проверка создания курьера без логина или пароля")
    @pytest.mark.parametrize("fields", ["login", "password"])
    def test_create_courier_without_required_fields(self, fields):
        payload = {"login": "test_login", "password": "test_password"}
        del payload[fields]

        response = requests.post(Urls.CREATE_COURIER_URL, data=payload)
        assert response.status_code == 400, f"Ожидали статус 400, а получили {response.status_code}"
        assert response.json().get('message') == Errors.COURIER_CREATE_DONT_HAVE_REQURED_FIELDS, f"Ожидали сообщение {Errors.COURIER_CREATE_DONT_HAVE_REQURED_FIELDS}, а получили {response.json().get('message')}"

    @allure.title("Проверка создания курьера с уже существующим логином")
    @allure.description("Проверка создания курьера с логином, который уже зарегистрирован")
    def test_create_courier_with_existing_login(self):
        payload = Payloads.ALREADY_REGISTERED_COURIER
        response = requests.post(Urls.CREATE_COURIER_URL, data=payload)
        assert response.status_code == 409, f"Ожидали статус 409, а получили {response.status_code}"
        assert response.json().get('message') == Errors.COURIER_ALREADY_CREATED, f"Ожидали сообщение {Errors.COURIER_ALREADY_CREATED}, а получили {response.json().get('message')}"
