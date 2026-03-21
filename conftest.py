import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from api_client.api_client import api_client
from pages.main_page import MainPage

@pytest.fixture(scope="session")
def api_client():
    """Фикстура для API клиента"""
    return api_client()


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



