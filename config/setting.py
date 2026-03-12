import os
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # API Settings
    API_BASE_URL: str = "https://market-delivery.yandex.ru/api/v2"

    # UI Settings
    UI_BASE_URL: str = "https://market.yandex.ru"

    # Test Data
    TEST_RESTAURANT_ID: str = os.getenv("TEST_RESTAURANT_ID", "12345")
    TEST_USER_TOKEN: str = os.getenv("TEST_USER_TOKEN", "test_token_123")
    TEST_PRODUCT_ID: str = os.getenv("TEST_PRODUCT_ID", "67890")

    # Browser Settings
    BROWSER: str = "chrome"
    HEADLESS: bool = False
    TIMEOUT: int = 10

    class Config:
        env_file = ".env"


settings = Settings()
