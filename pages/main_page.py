from data.test_data import TestData
import allure
from config.setting  import settings

class MainPage():
    """Page Object для главной страницы Яндекс маркет"""


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        """Открывает главную страницу"""
        self.open(settings.UI_BASE_URL)

    @allure.step("Поиск товара: {query}")
    def search_product(self, query: str):
        """Выполняет поиск товара"""
        self.type_text(TestData.SEARCH_INPUT, query)
        self.click(TestData.SEARCH_BUTTON)

    @allure.step("Получить информацию о ресторане")
    def get_restaurant_info(self) -> str:
        """Получает информацию о ресторане"""
        restaurant_card = self.find_element(TestData.RESTAURANT_CARD)
        return restaurant_card.text

    @allure.step("Получить информацию о меню")
    def get_menu_info(self) -> bool:
        """Проверяет наличие меню"""
        menu_elements = self.find_elements(TestData.MENU_SECTION)
        return len(menu_elements) > 0

    @allure.step("Получить время работы")
    def get_working_hours(self) -> str:
        """Получает время работы ресторана"""
        hours_element = self.find_element(TestData.WORKING_HOURS)
        return hours_element.text

    @allure.step("Перейти к авторизации")
    def go_to_auth(self):
        """Переходит на страницу авторизации"""
        self.click(TestData.LOGIN_BUTTON)

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        """Переходит в корзину"""
        self.click(TestData.CART_ICON)


def go_to_cart():
    return None