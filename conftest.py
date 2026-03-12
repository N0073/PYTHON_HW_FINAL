import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from api.client import APIClient
from pages.main_page import MainPage
from config.settings import settings


@pytest.fixture(scope="session")
def api_client():
    """Фикстура для API клиента"""
    return APIClient()


@pytest.fixture(scope="function")
def driver(request):
    """Фикстура для WebDriver"""
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def main_page(driver):
    """Фикстура для главной страницы"""
    page = MainPage(driver)
    page.open_main_page()
    return page



