import requests
import allure
from api_urls import Urls

class TestListOrders:
    @allure.title("Проверка получения списка заказов")
    @allure.description("Проверка получения списка заказов")
    def test_get_list_of_orders(self):
        response = requests.get(Urls.CREATE_ORDERD_URL)
        assert response.status_code == 200, f"Ожидали статус код 200, а получили {response.status_code}"
        assert response.text, "Ответ от сервера пустой"
        try:
            orders_list = response.json().get("orders")
        except ValueError as e:
            raise AssertionError(f"Ответ не является валидным JSON: {response.text}") from e
        assert isinstance(orders_list, list), "'orders' нет в листе"