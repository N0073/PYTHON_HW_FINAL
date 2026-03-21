import os
class settings:
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

        # config/endpoints.py

    ENDPOINTS = {
        "menu": "/api/v1/menu",
        "cart": "/api/v1/cart",
        "order": "/api/v1/orders",
        "restaurants": "/api/v1/restaurants",
    }


setting = settings()

