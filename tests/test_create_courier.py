import requests
import allure
import pytest

from api_urls import Urls
from data import Payloads, Errors

class TestCreatingCourier:
    
    @allure.title("Создание нового курьера")
    @allure.description("Проверка создания нового курьера, ответа и статус код(который должен быть равен 201)")
    def test_create_new_courier(self):
        payload = Payloads.generate_courier_payload()
        response = requests.post(Urls.CREATE_COURIER_URL, data=payload)
        print(response.status_code, response.json())
        assert response.status_code == 201, f"Ожидали статус код 201 а пришел {response.status_code}"
        assert response.json() == {"ok" : True}, f"Ожидали ответ ok true а пришел {response.json()}"
    
    @allure.title("Проверка создания двух одинаковых курьеров")
    @allure.description("Проверка создания двух одинаковых курьеров,ответа и статус код(который должен быть равен 409)")
    def test_create_identical_couriers(self):
        payload = Payloads.generate_courier_payload()
        first_courier = requests.post(Urls.CREATE_COURIER_URL,data=payload)
        if first_courier.status_code == 201:
            response = requests.post(Urls.CREATE_COURIER_URL, data=payload)
            assert response.status_code == 409, f"Ожидали статус код 409,а пришел {response.status_code}"
            assert response.json().get('message') == Errors.COURIER_ALREADY_CREATED, f"Ожидали сообщения {Errors.COURIER_ALREADY_CREATED} а пришло {response.json().get('message')}"

    @allure.title("Проверка создания курьера без обязательных полей")
    @allure.description("Проверка создания курьера без полей 'Пароль' и 'Логин'")
    @pytest.mark.parametrize("fields",["login","password"])
    def test_create_courier_without_passwords_and_login(self,fields):
        payload = Payloads.generate_courier_payload()
        if fields in payload:
            del payload[fields]
        
        response = requests.post(Urls.CREATE_COURIER_URL, data=payload)
        assert response.status_code == 400, f"Ожидали статус код 400 а получили {response.status_code}"
        assert response.json().get('message') == Errors.COURIER_CREATE_DONT_HAVE_REQURED_FIELDS, f"Ожадали сообщение {Errors.COURIER_CREATE_DONT_HAVE_REQURED_FIELDS} а получили {response.json.get('message')}"
    
    @allure.title("Проверка создания курьера c полем Login который уже был ранее зарегистрирован")
    @allure.description("Проверка создания курьера с Login который уже есть в базе данных")
    def test_create_courier_with_login_witch_already_used(self):
        payload = Payloads.ALREADY_REGISTERED_COURIER
        response = requests.post(Urls.CREATE_COURIER_URL, data=payload)
        assert response.status_code == 409, f"Ожидали статус код 409,а пришел {response.status_code}"
        assert response.json().get('message') == Errors.COURIER_ALREADY_CREATED, f"Ожидали сообщения {Errors.COURIER_ALREADY_CREATED} а пришло {response.json().get('message')}"
