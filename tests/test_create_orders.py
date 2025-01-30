import requests
import allure
import pytest
import json

from api_urls import Urls
from data import Payloads

class TestCreateOrders:
    
    @allure.title("Проверка создания заказа с разными цветами")
    @allure.description("Проверка создания заказа с разными цветами(и без них)")
    @pytest.mark.parametrize("order_payload",[Payloads.ORDER_COLOR_BLACK,
                                              Payloads.ORDER_COLOR_GRAY, 
                                              Payloads.ORDER_COLOR_BLACK_AND_GRAY, 
                                              Payloads.ORDER_WITHOUT_COLOR])
    def test_create_order_different_colors(self, order_payload):
        payload = json.dumps(order_payload)
        response = requests.post(Urls.CREATE_ORDERD_URL, data=payload)
        assert response.status_code == 201, f"Ожидали 201, а пришло {response.status_code}"
        assert "track" in response.json(), f"Ожидали поле track в ответе, а пришло {response.json()}"