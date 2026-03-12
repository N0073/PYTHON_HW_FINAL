import allure
import pytest
from api.client import api_client
from data.test_data import TestData
from config.settings import settings

@pytest.mark.api
class TestMarketDeliveryAPI:
    """API тесты для Яндекс.Маркет Доставки"""

    @allure.title("Получить меню ресторана")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_menu(self, api_client):
        """Тест получения меню ресторана"""
        response = api_client.get_menu(settings.TEST_RESTAURANT_ID)
        assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"


    @allure.title("Добавить товар в корзину")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_to_cart(self, api_client, setup_cart):
        """Тест добавления товара в корзину"""
        response = api_client.add_to_cart(
            settings.TEST_PRODUCT_ID,
            TestData.VALID_QUANTITY
        )
        assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
        data = response.json()
        assert data["product_id"] == settings.TEST_PRODUCT_ID
        assert data["quantity"] == TestData.VALID_QUANTITY


    @allure.title("Изменить количество товара в заказе")
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_order(self, api_client, setup_cart):
        """Тест изменения заказа"""
        # Сначала добавляем товар
        add_response = api_client.add_to_cart(
            settings.TEST_PRODUCT_ID,
            TestData.VALID_QUANTITY
        )
        order_id = add_response.json()["id"]

        # Изменяем количество
        update_data = {"quantity": 3}
        response = api_client.update_order(order_id, update_data)
        assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
        assert response.json()["quantity"] == 3

    @allure.title("Удалить заказ")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_order(self, api_client, setup_cart):
        """Тест удаления заказа"""
        # Сначала добавляем товар
        add_response = api_client.add_to_cart(
            settings.TEST_PRODUCT_ID,
            TestData.VALID_QUANTITY
        )
        order_id = add_response.json()["id"]

        # Удаляем заказ
        response = api_client.delete_order(order_id)

        assert response.status_code == 204, f"Ожидался статус 204, получен {response.status_code}"

        # Проверяем, что заказа больше нет
        check_response = api_client.get(f"/order/{order_id}")
        assert check_response.status_code == 404


    @allure.title("Негативный тест: добавление товара с нулевым количеством")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_with_zero_quantity(self, api_client, setup_cart):
        """Негативный тест добавления товара с количеством 0"""
        response = api_client.add_to_cart(
            settings.TEST_PRODUCT_ID,
            TestData.INVALID_QUANTITY
        )
        # Ожидаем ошибку 400 (Bad Request)
        assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"
        assert "error" in response.json(), "Ответ должен содержать поле 'error'"

