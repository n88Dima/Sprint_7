import pytest
import requests

from api_urls import Urls
from data import Payloads

@pytest.fixture
def courier():
    payload = Payloads.generate_courier_payload()
    response = requests.post(Urls.CREATE_COURIER_URL, data=payload)
    assert response.status_code == 201, f"Не удалось создать курьера, статус {response.status_code}, ответ: {response.json()}"

    login_response = requests.post(Urls.LOGIN_COURIER_URL, data=payload)
    assert login_response.status_code == 200, f"Не удалось залогинить курьера, статус {login_response.status_code}, ответ: {login_response.json()}"
    courier_id = login_response.json()["id"]

    yield payload

    delete_url = f"{Urls.DELETE_COURIER_URL}/{courier_id}"
    delete_response = requests.delete(delete_url)

    assert delete_response.status_code == 200, f"Ошибка удаления курьера: {delete_response.json()}"
