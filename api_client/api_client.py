import requests
import allure
from typing import Dict, Any
from config.setting import settings
from data.test_data import TestData

class APIClient:
    """Клиент для работы с API Яндекс доставки"""

    def __init__(self) -> None:
        self.base_url = settings.API_BASE_URL
        self.headers = {
            "Authorization": f"Bearer {settings.TEST_USER_TOKEN}",
            "Content-Type": "application/json"
        }

    @allure.step("GET запрос: {endpoint}")
    def get(self, endpoint: str, params: Dict = None) -> requests.Response:
        """Выполняет GET запрос"""
        url = f"{self.base_url}{endpoint}"
        return requests.get(url, headers=self.headers, params=params)

    @allure.step("POST запрос: {endpoint}")
    def post(self, endpoint: str, data: Dict = None) -> requests.Response:
        """Выполняет POST запрос"""
        url = f"{self.base_url}{endpoint}"
        return requests.post(url, headers=self.headers, json=data)

    @allure.step("PUT запрос: {endpoint}")
    def put(self, endpoint: str, data: Dict = None) -> requests.Response:
        """Выполняет PUT запрос"""
        url = f"{self.base_url}{endpoint}"
        return requests.put(url, headers=self.headers, json=data)

    @allure.step("DELETE запрос: {endpoint}")
    def delete(self, endpoint: str) -> requests.Response:
        """Выполняет DELETE запрос"""
        url = f"{self.base_url}{endpoint}"
        return requests.delete(url, headers=self.headers)

    @allure.step("Получить меню ресторана")
    def get_menu(self, restaurant_id: str) -> requests.Response:
        """Получает меню ресторана"""
        endpoint = TestData.ENDPOINTS["menu"]
        params = {"restaurant_id": restaurant_id}
        return self.get(endpoint, params)

    @allure.step("Добавить товар в корзину")
    def add_to_cart(self, product_id: str, quantity: int) -> requests.Response:
        """Добавляет товар в корзину"""
        endpoint = TestData.ENDPOINTS["cart"]
        data = {
            "product_id": product_id,
            "quantity": quantity
        }
        return self.post(endpoint, data)

    @allure.step("Изменить заказ")
    def update_order(self, order_id: str, updates: Dict[str, Any]) -> requests.Response:
        """Изменяет существующий заказ"""
        endpoint = f"{TestData.ENDPOINTS['order']}/{order_id}"
        return self.put(endpoint, updates)

    @allure.step("Удалить заказ")
    def delete_order(self, order_id: str) -> requests.Response:
        """Удаляет заказ"""
        endpoint = f"{TestData.ENDPOINTS['order']}/{order_id}"
        return self.delete(endpoint)


api_client = APIClient()
