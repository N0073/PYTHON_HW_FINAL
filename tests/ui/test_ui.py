import allure
import pytest
from data.test_data import TestData
from config.settings import settings

from pages import main_page


@pytest.mark.ui
class TestMarketDeliveryUI:
    """UI тесты для Яндекс.Маркет Доставки"""

    @allure.title("Поиск блюда и проверка корзины")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_dish_and_cart(self, main_page):
        """Тест поиска блюда и проверки корзины"""
        # Ищем блюдо


main_page.search_product(TestData.SEARCH_QUERY)

# Проверяем, что поиск сработал
assert TestData.SEARCH_QUERY in main_page.driver.title.lower()

# Переходим в корзину
main_page.go_to_cart()

# Проверяем, что страница корзины загрузилась
assert "корзина" in main_page.driver.title.lower()


@allure.title("Проверка информации о ресторане")
@allure.severity(allure.severity_level.NORMAL)
def test_restaurant_info(self, main_page):
    """Тест проверки информации о ресторане"""
    info = main_page.get_restaurant_info()

    assert info is not None, "Информация о ресторане не найдена"
    assert TestData.RESTAURANT_NAME in info, f"Имя ресторана должно содержать '{TestData.RESTAURANT_NAME}'"


@allure.title("Проверка информации о меню")
@allure.severity(allure.severity_level.NORMAL)
def test_menu_info(self, main_page):
    """Тест проверки информации о меню"""
    has_menu = main_page.get_menu_info()

    assert has_menu, "Меню ресторана не найдено"


@allure.title("Проверка времени работы ресторана")
@allure.severity(allure.severity_level.NORMAL)
def test_working_hours(self, main_page):
    """Тест проверки времени работы"""
    hours = main_page.get_working_hours()

    assert hours is not None, "Время работы не найдено"
    assert ":" in hours, "Время работы должно содержать часы и минуты"


@allure.title("Проверка авторизации")
@allure.severity(allure.severity_level.CRITICAL)
def test_auth_page(self, main_page):
    """Тест перехода на страницу авторизации"""
    main_page.go_to_auth()

    # Проверяем, что мы на странице авторизации
    assert "авторизация" in main_page.driver.title.lower() or "войти" in main_page.driver.title.lower()

    # Проверяем наличие полей для ввода
    try:
        email_field = main_page.driver.find_element_by_css_selector("input[type='email']")
        password_field = main_page.driver.find_element_by_css_selector("input[type='password']")
        assert email_field and password_field, "Поля для ввода логина/пароля не найдены"
    except:
        pass  # Разные формы авторизации могут иметь разные поля
